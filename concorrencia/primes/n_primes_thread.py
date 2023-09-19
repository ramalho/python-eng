#!/usr/bin/env python3

"""
n_primes_thread.py: useful only as a didactic example
of what NOT to do until Python's GIL is removed.

While the GIL is around, Python threads are slower
than good old sequential code for CPU-intensive tasks.
The GIL only allows one thread to run at a time, so
Python code only uses one CPU core.
"""

import sys
from time import perf_counter
from typing import NamedTuple
from threading import Thread  # <1>
from os import cpu_count
from queue import SimpleQueue  # <2>

from primes import is_prime, NUMBERS

class PrimeResult(NamedTuple):  # <3>
    n: int
    prime: bool
    elapsed: float

JobQueue = SimpleQueue[int]  # <4>
ResultQueue = SimpleQueue[PrimeResult]  # <5>

def check(n: int) -> PrimeResult:  # <6>
    t0 = perf_counter()
    res = is_prime(n)
    return PrimeResult(n, res, perf_counter() - t0)

def worker(jobs: JobQueue, results: ResultQueue) -> None:  # <7>
    while n := jobs.get():  # <8>
        results.put(check(n))  # <9>
    results.put(PrimeResult(0, False, 0.0))  # <10>

def start_jobs(
    procs: int, jobs: JobQueue, results: ResultQueue  # <11>
) -> None:
    for n in NUMBERS:
        jobs.put(n)  # <12>
    for _ in range(procs):
        proc = Thread(target=worker, args=(jobs, results))  # <13>
        proc.start()  # <14>
        jobs.put(0)  # <15>
# end::PRIMES_PROC_TOP[]

# tag::PRIMES_PROC_MAIN[]
def main() -> None:
    if len(sys.argv) < 2:  # <1>
        procs = cpu_count()
    else:
        procs = int(sys.argv[1])

    print(f'Checking {len(NUMBERS)} numbers with {procs} threads:')
    t0 = perf_counter()
    jobs: JobQueue = SimpleQueue()  # <2>
    results: ResultQueue = SimpleQueue()
    start_jobs(procs, jobs, results)  # <3>
    checked = report(procs, results)  # <4>
    elapsed = perf_counter() - t0
    print(f'{checked} checks in {elapsed:.2f}s')  # <5>

def report(procs: int, results: ResultQueue) -> int: # <6>
    checked = 0
    procs_done = 0
    while procs_done < procs:  # <7>
        n, prime, elapsed = results.get()  # <8>
        if n == 0:  # <9>
            procs_done += 1
        else:
            checked += 1  # <10>
            label = 'P' if prime else ' '
            print(f'{n:16}  {label} {elapsed:9.6f}s')
    return checked

if __name__ == '__main__':
    main()
# end::PRIMES_PROC_MAIN[]
