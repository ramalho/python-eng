#!/usr/bin/env python3

import time

from primes import is_prime


def main():
    n = 18_014_398_509_481_951
    t0 = time.perf_counter()
    primo = is_prime(n)
    e_nao_e = 'é' if primo else 'não é'
    elapsed = time.perf_counter() - t0
    print(f'{n:_d} {e_nao_e} primo ({elapsed:3.1f}s)')


if __name__ == '__main__':
    main()
