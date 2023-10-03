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
    Experiment(17592186044416, 2),  # 2 ** 44
    Experiment(17592186044399, 17592186044399),
    Experiment(17592236376019, 4194301),
    Experiment(281474976710656, 2),  # 2 ** 48
    Experiment(281474976710597, 281474976710597),
    Experiment(281475647799167, 16777213),
    Experiment(4503599627370496, 2),  # 2 ** 52
    Experiment(4503599627370449, 4503599627370449),
    Experiment(4503600298459061, 67108859),
    Experiment(72057594037927936, 2),  # 2 ** 56
    Experiment(72057594037927931, 72057594037927931),
    Experiment(72057596722278677, 268435399),
    Experiment(1152921504606846976, 2),  # 2 ** 60
    Experiment(1152921504606846883, 1152921504606846883),
    Experiment(1152921538966582999, 1073741789),
    Experiment(18446744073709551615, 3),  # 2 ** 64 - 1
    Experiment(18446744073709551557, 18446744073709551557),  # costly!
    Experiment(18446744030759878681, 4294967291),  # costly!
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
        print(f'{label}  {pair.n:20}  {pair.lpf:20}  {elapsed:9.6f}s')


if __name__ == '__main__':
    auto_test()
