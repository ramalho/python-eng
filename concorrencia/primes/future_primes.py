#!/usr/bin/env python3

# machine	2 **
# RPI42 	49
# X250		53
# YOGA		57
# M2MAX		57
# VIVO		63

from concurrent.futures import ProcessPoolExecutor
from time import perf_counter
from primes import NUMBERS, least_prime_factor

POWER_OF_TWO = 2**57


def make_sample(power_of_two):
    for i, n in enumerate(NUMBERS):
        if n > power_of_two:
            last = i
            break
    stop = last + 1
    return NUMBERS[stop - 21 : stop]


def main():
    sample = make_sample(POWER_OF_TWO)
    t0 = perf_counter()
    with ProcessPoolExecutor() as executor:
        for number, lfp in zip(sample, executor.map(least_prime_factor, sample)):
            separator = ' = ' if number == lfp else '   '
            print(f'{number:26_d} {separator} {lfp:26_d}')
    elapsed = perf_counter() - t0
    print(f'{len(sample)} checks in {elapsed:.1f}s')


if __name__ == '__main__':
    main()
