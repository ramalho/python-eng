#!/usr/bin/env python3

import math
import time
import typing


class Experiment(typing.NamedTuple):
    n: int
    lpf: int

    @property
    def prime(self):
        return self.n == self.lpf


EXPERIMENTS = [
    Experiment(61, 61),  # prime
    Experiment(64, 2),  # 2 ** 6
    Experiment(77, 7),  # semiprime
    Experiment(134_217_689, 134217689),  # prime
    Experiment(134_217_728, 2),  # 2 ** 27
    Experiment(134_235_347, 11579),  # semiprime
    Experiment(8_589_934_583, 8589934583),  # prime
    Experiment(8_589_934_592, 2),  # 2 ** 33
    Experiment(8_589_953_123, 92681),  # semiprime
    Experiment(549_755_813_881, 549755813881),  # prime
    Experiment(549_755_813_888, 2),  # 2 ** 39
    Experiment(549_755_516_449, 741431),  # semiprime
    Experiment(35_184_372_088_777, 35184372088777),  # prime
    Experiment(35_184_372_088_832, 2),  # 2 ** 45
    Experiment(35_184_412_406_009, 5931641),  # semiprime
    Experiment(2_251_799_813_685_119, 2251799813685119),  # prime
    Experiment(2_251_799_813_685_248, 2),  # 2 ** 51
    Experiment(2_251_800_685_671_203, 47453111),  # semiprime
    Experiment(144_115_188_075_855_859, 144115188075855859),  # prime
    Experiment(144_115_188_075_855_872, 2),  # 2 ** 57
    Experiment(144_115_189_976_253_901, 379625047),  # semiprime
    Experiment(9_223_372_036_854_775_783, 9223372036854775783),  # prime
    Experiment(9_223_372_036_854_775_808, 2),  # 2 ** 63
    Experiment(9_223_372_037_000_249_951, 3037000493),  # semiprime
    Experiment(18_446_744_073_709_551_557, 18446744073709551557),  # prime
    Experiment(18_446_744_073_709_551_615, 3),  # 2 ** 64 - 1
    Experiment(18_446_744_030_759_878_681, 4294967291),  # semiprime
]


NUMBERS = [n for n, _ in EXPERIMENTS]


def least_prime_factor(n: int) -> int:
    """Returns the least prime pactor of `n`.
    When `n` is prime, the return value is `n`.
    """
    if n == 1:
        return 1
    if n % 2 == 0:
        return 2
    if n % 3 == 0:
        return 3

    # using the 6k+-1 algorithm
    limit = math.isqrt(n)
    for i in range(5, limit + 1, 6):
        if n % i == 0:
            return i
        j = i + 2
        if n % j == 0:
            return j
    return n


def is_prime(n: int) -> bool:
    if n <= 1:
        return False
    return least_prime_factor(n) == n


def auto_test():
    """Test is_prime() with EXPERIMENTS"""
    t0 = time.perf_counter()
    for exp in EXPERIMENTS:
        t = time.perf_counter()
        lpf_result = least_prime_factor(exp.n)
        elapsed = time.perf_counter() - t
        assert lpf_result == exp.lpf, f'wrong LPF {lpf_result} for {exp.n}'
        label = 'P' if exp.prime else ' '
        print(f'{exp.n:26_d}  {label}  {exp.lpf:26_d}  {elapsed:9.6f}s')
    elapsed = time.perf_counter() - t
    print(f'{len(EXPERIMENTS)} checks in {elapsed:.2f}s')  # <5>


if __name__ == '__main__':
    auto_test()
