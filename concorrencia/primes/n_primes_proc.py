#!/usr/bin/env python3

"""
n_primes_proc.py: shows that multiprocessing on a multicore machine
can be faster than sequential code for CPU-intensive work.

This is a DIY implementation of the worker pool pattern: the main
program starts a number of worker processes which read integers
from a queue, checks whether each integer is prime, and and posts
results into another queue which is consumed by a function that
displays the results.
"""

import sys
from time import perf_counter
from typing import NamedTuple
from multiprocessing import Process, SimpleQueue, cpu_count  # <1>
from multiprocessing import queues  # <2>

from primes import least_prime_factor, make_sample

"""
Using `fork` to fix FileNotFoundError happening on MacOS 13.6 (Ventura)
using Python 3.11 or 3.12.0 installed from images on python.org.
The FileNotFoundError does not happen using PyPy 7.3.12 (~Python 3.10.12).

Traceback (most recent call last):
  File "<string>", line 1, in <module>
  File "/Library/Frameworks/Python.framework/Versions/3.12/lib/python3.12/multiprocessing/spawn.py", line 122, in spawn_main
    exitcode = _main(fd, parent_sentinel)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Library/Frameworks/Python.framework/Versions/3.12/lib/python3.12/multiprocessing/spawn.py", line 132, in _main
    self = reduction.pickle.load(from_parent)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Library/Frameworks/Python.framework/Versions/3.12/lib/python3.12/multiprocessing/synchronize.py", line 115, in __setstate__
    self._semlock = _multiprocessing.SemLock._rebuild(*state)
                    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
FileNotFoundError: [Errno 2] No such file or directory

Fix mentioned here:
https://superfastpython.com/filenotfounderror-multiprocessing-python/

"""
from multiprocessing import set_start_method

set_start_method('fork')

# Magnitude of primes that take a few seconds to check
#
# machine  magnitude
# RPI4     2 ** 49
# X250     2 ** 53
# YOGA9    2 ** 57
# M2MAX    2 ** 57
# VIVO     2 ** 63

MAGNITUDE = 2**57


class Experiment(NamedTuple):  # <3>
    n: int
    lpf: int
    elapsed: float

    @property
    def prime(self):
        return self.n == self.lpf


JobQueue = queues.SimpleQueue[int]  # <4>
ResultQueue = queues.SimpleQueue[Experiment]  # <5>


def check(n: int) -> Experiment:  # <6>
    t0 = perf_counter()
    res = least_prime_factor(n)
    return Experiment(n, res, perf_counter() - t0)


def worker(jobs: JobQueue, results: ResultQueue) -> None:  # <7>
    while n := jobs.get():  # <8>
        results.put(check(n))  # <9>
    results.put(Experiment(0, False, 0.0))  # <10>


def start_jobs(qtd_procs: int, results: ResultQueue) -> None:
    jobs: JobQueue = SimpleQueue()  # <2>
    for n in make_sample(MAGNITUDE):
        jobs.put(n)  # <12>
    for _ in range(qtd_procs):
        proc = Process(target=worker, args=(jobs, results))  # <13>
        proc.start()  # <14>
        jobs.put(0)  # <15> "poison pill"


def report(qtd_procs: int, results: ResultQueue) -> int:  # <6>
    checked = 0
    procs_done = 0
    while procs_done < qtd_procs:  # <7>
        exp = results.get()  # <8>
        if exp.n == 0:  # <9>
            procs_done += 1
        else:
            checked += 1  # <10>
            label = '=' if exp.prime else ' '
            print(f'{exp.n:26_d}  {label}  {exp.lpf:26_d}  {exp.elapsed:9.6f}s')
    return checked


def main() -> None:
    if len(sys.argv) < 2:  # <1>
        qtd_procs = cpu_count()
    else:
        qtd_procs = int(sys.argv[1])

    print(f'Using {qtd_procs} worker processes.')
    t0 = perf_counter()
    results: ResultQueue = SimpleQueue()
    start_jobs(qtd_procs, results)  # <3>
    checked = report(qtd_procs, results)  # <4>
    elapsed = perf_counter() - t0
    print(f'{checked} checks in {elapsed:.1f}s')  # <5>

if __name__ == '__main__':
    main()
