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


PRIME_FIXTURE = [
    Experiment(2, 2),  # 2 ** 1
    Experiment(3, 3),
    Experiment(4, 2),  # 2 ** 2
    Experiment(77, 7),
    Experiment(18014398509481951, 18014398509481951),
    Experiment(18014398509481984, 2),  # 2 ** 54
    Experiment(18014399314786597, 134217689),
    Experiment(72057594037927931, 72057594037927931),
    Experiment(72057594037927936, 2),  # 2 ** 56
    Experiment(72057596722278677, 268435399),
    Experiment(288230376151711717, 288230376151711717),
    Experiment(288230376151711744, 2),  # 2 ** 58
    Experiment(288230380446679007, 536870909),
    Experiment(1152921504606846883, 1152921504606846883),
    Experiment(1152921504606846976, 2),  # 2 ** 60
    Experiment(1152921538966582999, 1073741789),
    Experiment(4611686018427387847, 4611686018427387847),
    Experiment(4611686018427387904, 2),  # 2 ** 62
    Experiment(4611686039902224373, 2147483647),
    Experiment(18446744073709551557, 18446744073709551557),
    Experiment(18446744073709551615, 3),  # 2 ** 64 - 1
    Experiment(18446744030759878681, 4294967291),
]


NUMBERS = [n for n, _ in PRIME_FIXTURE]


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
    """Test is_prime() with PRIME_FIXTURE"""
    for pair in PRIME_FIXTURE:
        start = time.perf_counter()
        lpf_result = least_prime_factor(pair.n)
        elapsed = time.perf_counter() - start
        assert lpf_result == pair.lpf, f'wrong LPF {lpf_result} for {pair.n}'
        label = 'P' if pair.prime else ' '
        print(f'{label}  {pair.n:26_d}  {pair.lpf:26_d}  {elapsed:9.6f}s')


if __name__ == '__main__':
    auto_test()
