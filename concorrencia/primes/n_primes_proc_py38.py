#!/usr/bin/env pypy3

"""
n_primes_proc_py38.py is the same as n_primes_proc.py without some
parameterized generic types, for compatibility with older versions
of Python or Pypy.

This examples shows that multiprocessing on a multicore machine
can be faster than sequential code for CPU-intensive work.

This is a DIY implementation of the worker pool pattern: the main
program starts a number of worker processes which read integers
from a queue, checkes wether they are prime, and and posts results
into another queue which is used to generate a report on stdout.
"""

import sys
from time import perf_counter
from typing import NamedTuple
from multiprocessing import Process, SimpleQueue, cpu_count  # <1>
from multiprocessing import queues  # <2>

from primes import is_prime, NUMBERS


class PrimeResult(NamedTuple):  # <3>
    n: int
    prime: bool
    elapsed: float


JobQueue = queues.SimpleQueue  # <4>
ResultQueue = queues.SimpleQueue  # <5>


def check(n: int) -> PrimeResult:  # <6>
    t0 = perf_counter()
    res = is_prime(n)
    return PrimeResult(n, res, perf_counter() - t0)


def worker(jobs: JobQueue, results: ResultQueue) -> None:  # <7>
    while n := jobs.get():  # <8>
        results.put(check(n))  # <9>
    results.put(PrimeResult(0, False, 0.0))  # <10>


def start_jobs(
    qtd_procs: int, jobs: JobQueue, results: ResultQueue  # <11>
) -> None:
    for n in NUMBERS:
        jobs.put(n)  # <12>
    for _ in range(qtd_procs):
        proc = Process(target=worker, args=(jobs, results))  # <13>
        proc.start()  # <14>
        jobs.put(0)  # <15> "poison pill"


def report(qtd_procs: int, results: ResultQueue) -> int:   # <6>
    checked = 0
    procs_done = 0
    while procs_done < qtd_procs:  # <7>
        n, prime, elapsed = results.get()  # <8>
        if n == 0:  # <9>
            procs_done += 1
        else:
            checked += 1  # <10>
            label = 'P' if prime else ' '
            print(f'{n:16}  {label} {elapsed:9.6f}s')
    return checked


def main() -> None:
    if len(sys.argv) < 2:  # <1>
        qtd_procs = cpu_count()
    else:
        qtd_procs = int(sys.argv[1])

    print(f'Checking {len(NUMBERS)} numbers with {qtd_procs} processes:')
    t0 = perf_counter()
    jobs: JobQueue = SimpleQueue()  # <2>
    results: ResultQueue = SimpleQueue()
    start_jobs(qtd_procs, jobs, results)  # <3>
    checked = report(qtd_procs, results)  # <4>
    elapsed = perf_counter() - t0
    print(f'{checked} checks in {elapsed:.2f}s')  # <5>


if __name__ == '__main__':
    main()
