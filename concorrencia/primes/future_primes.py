#!/usr/bin/env python3


from concurrent.futures import ProcessPoolExecutor
from time import perf_counter
from primes import least_prime_factor, make_sample, LeastPrimeFactor

# Power of two that takes about 3 seconds to compute
# machine	2 **
# RPI42 	49
# X250		53
# YOGA		57
# M2MAX		57
# VIVO		63

LARGEST = 2**57


def check_lpf(n: int) -> tuple[LeastPrimeFactor, float]:
    t0 = perf_counter()
    lpf = LeastPrimeFactor(n, least_prime_factor(n))
    elapsed = perf_counter() - t0
    return (lpf, elapsed)


def main():
    sample = make_sample(LARGEST)
    t0 = perf_counter()
    processing_time = 0
    with ProcessPoolExecutor() as executor:
        for lpf, elapsed in executor.map(check_lpf, sample):
            separator = ' = ' if  lpf.n == lpf.factor else '   '
            print(f'{lpf.n:26_d} {separator} {lpf.factor:26_d}  ({elapsed:9.5f}s)')
            processing_time += elapsed
    elapsed = perf_counter() - t0
    print(f'{len(sample)} checks in {elapsed:.1f}s')
    print(f'Total processing time: {processing_time:.1f}s')


if __name__ == '__main__':
    main()
