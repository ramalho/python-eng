#!/usr/bin/env python3

import sys
import time
from operator import attrgetter
from primes import EXPERIMENTS, is_prime

__doc__ = f"""
{sys.argv[0]} finds a prime number that takes "about" TIME seconds to check.

USAGE:
    {sys.argv[0]} TIME
""".strip()

primes = [exp.n for exp in EXPERIMENTS if exp.prime]
primes.sort()


def time_cost(n):
    t0 = time.perf_counter()
    is_prime(n)
    return time.perf_counter() - t0


def main():
    try:
        target_time = float(sys.argv[1])
    except (IndexError, ValueError):
        print(__doc__)
        sys.exit(-1)

    start = 0
    end = len(primes)
    delta = sys.maxsize

    while end - start > 1:
        middle = (start + end) // 2
        pick = primes[middle]
        print(f'{start:2}:{end:<2} [{middle:2}]     {pick:26_}', end=' ', flush=True)
        t = time_cost(pick)
        print(f'({t:.3f}s)')
        if t <= target_time:
            start = middle
        else:
            end = middle

    marker = '^' * len(f'{pick:_}')
    print(f'Closest prime  {marker:>26}')


if __name__ == '__main__':
    main()
