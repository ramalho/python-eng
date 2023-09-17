#!/usr/bin/env python3

from math import isqrt

PRIME_FIXTURE = [
    (2, True),
    (142702110479723, True),
    (299593572317531, True),
    (3333333333333301, True),
    (3333333333333333, False),
    (3333335652092209, False),
    (4444444444444423, True),
    (4444444444444444, False),
    (4444444488888889, False),
    (5555553133149889, False),
    (5555555555555503, True),
    (5555555555555555, False),
    (6666666666666666, False),
    (6666666666666719, True),
    (6666667141414921, False),
    (7777777536340681, False),
    (7777777777777753, True),
    (7777777777777777, False),
    (9999999999999917, True),
    (9999999999999999, False),
]


NUMBERS = [n for n, _ in PRIME_FIXTURE]


def is_prime(n: int) -> bool:
    """Using 6k+-1 algorithm"""
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False

    limit = isqrt(n)
    for i in range(5, limit + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True


def auto_test():
    """Test is_prime() with PRIME_FIXTURE"""
    for n, prime in PRIME_FIXTURE:
        prime_res = is_prime(n)
        assert prime_res == prime
        print(n, prime)


if __name__ == '__main__':
    auto_test()
