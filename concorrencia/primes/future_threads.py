#!/usr/bin/env python3

import os
import sys
import time
from concurrent import futures

from primes import least_prime_factor, make_sample, LeastPrimeFactor

# Magnitude of primes that take a few seconds to check
#
# machine  magnitude
# RPI4     2 ** 49
# X250     2 ** 53
# YOGA9    2 ** 57
# M2MAX    2 ** 57
# VIVO     2 ** 63

MAGNITUDE = 2**57


def check_lpf(n: int) -> tuple[LeastPrimeFactor, float]:
    t0 = time.perf_counter()
    lpf = LeastPrimeFactor(n, least_prime_factor(n))
    elapsed = time.perf_counter() - t0
    return (lpf, elapsed)


def main():
    if len(sys.argv) < 2:  # <1>
        qtd_procs = os.cpu_count()
    else:
        qtd_procs = int(sys.argv[1])

    sample = make_sample(MAGNITUDE)
    t0 = time.perf_counter()
    processing_time = 0
    with futures.ThreadPoolExecutor(max_workers=qtd_procs) as executor:
        tasks = (executor.submit(check_lpf, n) for n in sample)
        for future in futures.as_completed(tasks):
            lpf, elapsed = future.result()
            separator = '=' if lpf.prime else ' '
            print(f'{lpf.n:26_d} {separator} {lpf.factor:26_d}  ({elapsed:9.5f}s)')
            processing_time += elapsed
    elapsed = time.perf_counter() - t0
    print(f'{len(sample)} checks in {elapsed:.1f}s')
    print(f'Total processing time: {processing_time:.1f}s using {qtd_procs} threads.')


if __name__ == '__main__':
    main()
