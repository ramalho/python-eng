#!/usr/bin/env python3

import math
import time
import typing


class PrimeResult(typing.NamedTuple):
    n: int
    lpf: int

    @property
    def prime(self):
        return self.n == self.lpf


EXPERIMENTS = [
    PrimeResult(61, 61),  # prime
    PrimeResult(64, 2),  # 2 ** 6
    PrimeResult(77, 7),  # semiprime
    PrimeResult(134217689, 134217689),  # prime
    PrimeResult(134217728, 2),  # 2 ** 27
    PrimeResult(134235347, 11579),  # semiprime
    PrimeResult(536870909, 536870909),  # prime
    PrimeResult(536870912, 2),  # 2 ** 29
    PrimeResult(536848891, 23167),  # semiprime
    PrimeResult(2147483647, 2147483647),  # prime
    PrimeResult(2147483648, 2),  # 2 ** 31
    PrimeResult(2147673613, 46337),  # semiprime
    PrimeResult(8589934583, 8589934583),  # prime
    PrimeResult(8589934592, 2),  # 2 ** 33
    PrimeResult(8589953123, 92681),  # semiprime
    PrimeResult(34359738337, 34359738337),  # prime
    PrimeResult(34359738368, 2),  # 2 ** 35
    PrimeResult(34360553947, 185363),  # semiprime
    PrimeResult(137438953447, 137438953447),  # prime
    PrimeResult(137438953472, 2),  # 2 ** 37
    PrimeResult(137448888757, 370723),  # semiprime
    PrimeResult(549755813881, 549755813881),  # prime
    PrimeResult(549755813888, 2),  # 2 ** 39
    PrimeResult(549755516449, 741431),  # semiprime
    PrimeResult(2199023255531, 2199023255531),  # prime
    PrimeResult(2199023255552, 2),  # 2 ** 41
    PrimeResult(2199030965533, 1482907),  # semiprime
    PrimeResult(8796093022151, 8796093022151),  # prime
    PrimeResult(8796093022208, 2),  # 2 ** 43
    PrimeResult(8796165383693, 2965819),  # semiprime
    PrimeResult(35184372088777, 35184372088777),  # prime
    PrimeResult(35184372088832, 2),  # 2 ** 45
    PrimeResult(35184412406009, 5931641),  # semiprime
    PrimeResult(140737488355213, 140737488355213),  # prime
    PrimeResult(140737488355328, 2),  # 2 ** 47
    PrimeResult(140737507264631, 11863279),  # semiprime
    PrimeResult(562949953421231, 562949953421231),  # prime  # 3.3s on RPi 4
    PrimeResult(562949953421312, 2),  # 2 ** 49
    PrimeResult(562950123964819, 23726561),  # semiprime
    PrimeResult(2251799813685119, 2251799813685119),  # prime
    PrimeResult(2251799813685248, 2),  # 2 ** 51
    PrimeResult(2251800685671203, 47453111),  # semiprime
    PrimeResult(9007199254740881, 9007199254740881),  # prime
    PrimeResult(9007199254740992, 2),  # 2 ** 53
    PrimeResult(9007200654749953, 94906249),  # semiprime
    PrimeResult(36028797018963913, 36028797018963913),  # prime
    PrimeResult(36028797018963968, 2),  # 2 ** 55
    PrimeResult(36028803757875637, 189812507),  # semiprime
    PrimeResult(144115188075855859, 144115188075855859),  # prime  # 3.7s on MacStudio M2 Max
    PrimeResult(144115188075855872, 2),  # 2 ** 57
    PrimeResult(144115189976253901, 379625047),  # semiprime
    PrimeResult(576460752303423433, 576460752303423433),  # prime
    PrimeResult(576460752303423488, 2),  # 2 ** 59
    PrimeResult(576460752312515429, 759250111),  # semiprime
    PrimeResult(2305843009213693951, 2305843009213693951),  # prime
    PrimeResult(2305843009213693952, 2),  # 2 ** 61
    PrimeResult(2305843018361062409, 1518500213),  # semiprime
    PrimeResult(9223372036854775783, 9223372036854775783),  # prime
    PrimeResult(9223372036854775808, 2),  # 2 ** 63
    PrimeResult(9223372037000249951, 3037000493),  # semiprime
    PrimeResult(18446744073709551557, 18446744073709551557),  # prime
    PrimeResult(18446744073709551616, 2),  # 2 ** 64
    PrimeResult(18446744030759878681, 4294967291),  # semiprime
]


NUMBERS = (n for n, _ in EXPERIMENTS)


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
    limit = math.isqrt(int(n))
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
        t1 = time.perf_counter()
        lpf_result = least_prime_factor(exp.n)
        elapsed = time.perf_counter() - t1
        assert lpf_result == exp.lpf, f'wrong LPF {lpf_result} for {exp.n}'
        label = '=' if exp.prime else ' '
        print(f'{exp.n:26_d}  {label}  {exp.lpf:26_d}  {elapsed:9.6f}s')
    elapsed = time.perf_counter() - t0
    print(f'{len(EXPERIMENTS)} checks in {elapsed:.2f}s')  # <5>


if __name__ == '__main__':
    auto_test()
