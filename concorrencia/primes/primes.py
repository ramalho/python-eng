#!/usr/bin/env python3

import math
import time
import typing


class LeastPrimeFactor(typing.NamedTuple):
    n: int
    factor: int

    @property
    def prime(self):
        return self.n == self.factor


EXPERIMENTS = [
    LeastPrimeFactor(1099511627689, 1099511627689),  # prime
    LeastPrimeFactor(1099511627776, 2),  # 2 ** 40
    LeastPrimeFactor(1099515822059, 1048573),  # semiprime
    LeastPrimeFactor(1649267441651, 1649267441651),  # prime
    LeastPrimeFactor(1649267441664, 2),
    LeastPrimeFactor(1649280082649, 1284223),  # semiprime
    LeastPrimeFactor(2199023255531, 2199023255531),  # prime
    LeastPrimeFactor(2199023255552, 2),  # 2 ** 41
    LeastPrimeFactor(2199030965533, 1482907),  # semiprime
    LeastPrimeFactor(3298534883309, 3298534883309),  # prime
    LeastPrimeFactor(3298534883328, 2),
    LeastPrimeFactor(3298535218969, 1816187),  # semiprime
    LeastPrimeFactor(4398046511093, 4398046511093),  # prime
    LeastPrimeFactor(4398046511104, 2),  # 2 ** 42
    LeastPrimeFactor(4398063288167, 2097143),  # semiprime
    LeastPrimeFactor(6597069766631, 6597069766631),  # prime
    LeastPrimeFactor(6597069766656, 2),
    LeastPrimeFactor(6597074099513, 2568473),  # semiprime
    LeastPrimeFactor(8796093022151, 8796093022151),  # prime
    LeastPrimeFactor(8796093022208, 2),  # 2 ** 43
    LeastPrimeFactor(8796165383693, 2965819),  # semiprime
    LeastPrimeFactor(13194139533299, 13194139533299),  # prime
    LeastPrimeFactor(13194139533312, 2),
    LeastPrimeFactor(13194155405351, 3632371),  # semiprime
    LeastPrimeFactor(17592186044399, 17592186044399),  # prime
    LeastPrimeFactor(17592186044416, 2),  # 2 ** 44
    LeastPrimeFactor(17592236376019, 4194301),  # semiprime
    LeastPrimeFactor(26388279066623, 26388279066623),  # prime
    LeastPrimeFactor(26388279066624, 2),
    LeastPrimeFactor(26388378589219, 5136947),  # semiprime
    LeastPrimeFactor(35184372088777, 35184372088777),  # prime  # 0.8s on RPi 4 Cortex A72
    LeastPrimeFactor(35184372088832, 2),  # 2 ** 45
    LeastPrimeFactor(35184412406009, 5931641),  # semiprime
    LeastPrimeFactor(52776558133177, 52776558133177),  # prime
    LeastPrimeFactor(52776558133248, 2),
    LeastPrimeFactor(52776578032901, 7264739),  # semiprime
    LeastPrimeFactor(70368744177439, 8388593),  # semiprime
    LeastPrimeFactor(70368744177643, 70368744177643),  # prime
    LeastPrimeFactor(70368744177664, 2),  # 2 ** 46
    LeastPrimeFactor(105553116266489, 105553116266489),  # prime
    LeastPrimeFactor(105553116266496, 2),
    LeastPrimeFactor(105553165044073, 10273883),  # semiprime
    LeastPrimeFactor(140737488355213, 140737488355213),  # prime
    LeastPrimeFactor(140737488355328, 2),  # 2 ** 47
    LeastPrimeFactor(140737507264631, 11863279),  # semiprime
    LeastPrimeFactor(211106224954241, 14529467),  # semiprime
    LeastPrimeFactor(211106232532969, 211106232532969),  # prime
    LeastPrimeFactor(211106232532992, 2),
    LeastPrimeFactor(281474976710597, 281474976710597),  # prime
    LeastPrimeFactor(281474976710656, 2),  # 2 ** 48
    LeastPrimeFactor(281475647799167, 16777213),  # semiprime
    LeastPrimeFactor(422212465065953, 422212465065953),  # prime
    LeastPrimeFactor(422212465065984, 2),
    LeastPrimeFactor(422212701274081, 20547803),  # semiprime
    LeastPrimeFactor(562949953421231, 562949953421231),  # prime  # 3.3s on RPi 4 Cortex A72
    LeastPrimeFactor(562949953421312, 2),  # 2 ** 49
    LeastPrimeFactor(562950123964819, 23726561),  # semiprime
    LeastPrimeFactor(844424930131963, 844424930131963),  # prime  # 1.1s on ThinkPad X250 i7-5600U
    LeastPrimeFactor(844424930131968, 2),
    LeastPrimeFactor(844425248527967, 29058989),  # semiprime
    LeastPrimeFactor(1125899906842597, 1125899906842597),  # prime
    LeastPrimeFactor(1125899906842624, 2),  # 2 ** 50
    LeastPrimeFactor(1125899973949889, 33554393),  # semiprime
    LeastPrimeFactor(1688849860263901, 1688849860263901),  # prime
    LeastPrimeFactor(1688849860263936, 2),
    LeastPrimeFactor(1688849900993161, 41095619),  # semiprime
    LeastPrimeFactor(2251799813685119, 2251799813685119),  # prime
    LeastPrimeFactor(2251799813685248, 2),  # 2 ** 51
    LeastPrimeFactor(2251800685671203, 47453111),  # semiprime
    LeastPrimeFactor(3377699715516361, 58117981),  # semiprime
    LeastPrimeFactor(3377699720527861, 3377699720527861),  # prime
    LeastPrimeFactor(3377699720527872, 2),
    LeastPrimeFactor(4503599627370449, 4503599627370449),  # prime
    LeastPrimeFactor(4503599627370496, 2),  # 2 ** 52
    LeastPrimeFactor(4503600298459061, 67108859),  # semiprime
    LeastPrimeFactor(6755399441055731, 6755399441055731),  # prime  # 3.0s on ThinkPad X250 i7-5600U
    LeastPrimeFactor(6755399441055744, 2),
    LeastPrimeFactor(6755400425876213, 82191149),  # semiprime
    LeastPrimeFactor(9007199254740881, 9007199254740881),  # prime  # 1.2s on MacStudio M2 Max
    LeastPrimeFactor(9007199254740992, 2),  # 2 ** 53
    LeastPrimeFactor(9007200654749953, 94906249),  # semiprime
    LeastPrimeFactor(13510798882111483, 13510798882111483),  # prime  # 1.0s on Yoga 9i i7-1360P
    LeastPrimeFactor(13510798882111488, 2),
    LeastPrimeFactor(13510800489368561, 116235949),  # semiprime
    LeastPrimeFactor(18014398509481951, 18014398509481951),  # prime
    LeastPrimeFactor(18014398509481984, 2),  # 2 ** 54
    LeastPrimeFactor(18014399314786597, 134217689),  # semiprime
    LeastPrimeFactor(27021597764222939, 27021597764222939),  # prime
    LeastPrimeFactor(27021597764222976, 2),
    LeastPrimeFactor(27021598744655129, 164382457),  # semiprime
    LeastPrimeFactor(36028797018963913, 36028797018963913),  # prime
    LeastPrimeFactor(36028797018963968, 2),  # 2 ** 55
    LeastPrimeFactor(36028803757875637, 189812507),  # semiprime
    LeastPrimeFactor(54043195528445869, 54043195528445869),  # prime
    LeastPrimeFactor(54043195528445952, 2),
    LeastPrimeFactor(54043196378148947, 232471903),  # semiprime
    LeastPrimeFactor(72057594037927931, 72057594037927931),  # prime
    LeastPrimeFactor(72057594037927936, 2),  # 2 ** 56
    LeastPrimeFactor(72057596722278677, 268435399),  # semiprime
    LeastPrimeFactor(108086391056891903, 108086391056891903),  # prime  # 3.1s on Yoga 9i i7-1360P
    LeastPrimeFactor(108086391056891904, 2),
    LeastPrimeFactor(108086392348502419, 328764941),  # semiprime
    LeastPrimeFactor(144115188075855859, 144115188075855859),  # prime  # 3.7s on MacStudio M2 Max
    LeastPrimeFactor(144115188075855872, 2),  # 2 ** 57
    LeastPrimeFactor(144115189976253901, 379625047),  # semiprime
    LeastPrimeFactor(216172782113783773, 216172782113783773),  # prime
    LeastPrimeFactor(216172782113783808, 2),
    LeastPrimeFactor(216172794811474819, 464943847),  # semiprime
    LeastPrimeFactor(288230376151711717, 288230376151711717),  # prime
    LeastPrimeFactor(288230376151711744, 2),  # 2 ** 58
    LeastPrimeFactor(288230380446679007, 536870909),  # semiprime
    LeastPrimeFactor(432345564227567561, 432345564227567561),  # prime
    LeastPrimeFactor(432345564227567616, 2),
    LeastPrimeFactor(432345575969308769, 657529889),  # semiprime
    LeastPrimeFactor(576460752303423433, 576460752303423433),  # prime
    LeastPrimeFactor(576460752303423488, 2),  # 2 ** 59
    LeastPrimeFactor(576460752312515429, 759250111),  # semiprime
    LeastPrimeFactor(864691128455135207, 864691128455135207),  # prime
    LeastPrimeFactor(864691128455135232, 2),
    LeastPrimeFactor(864691136471065301, 929887691),  # semiprime
    LeastPrimeFactor(1152921504606846883, 1152921504606846883),  # prime
    LeastPrimeFactor(1152921504606846976, 2),  # 2 ** 60
    LeastPrimeFactor(1152921538966582999, 1073741789),  # semiprime
    LeastPrimeFactor(1729382256910270433, 1729382256910270433),  # prime
    LeastPrimeFactor(1729382256910270464, 2),
    LeastPrimeFactor(1729382303877233891, 1315059763),  # semiprime
    LeastPrimeFactor(2305843009213693951, 2305843009213693951),  # prime  # 1.2s on Vivobook Pro i9-11900H
    LeastPrimeFactor(2305843009213693952, 2),  # 2 ** 61
    LeastPrimeFactor(2305843018361062409, 1518500213),  # semiprime
    LeastPrimeFactor(3458764513820540791, 3458764513820540791),  # prime
    LeastPrimeFactor(3458764513820540928, 2),
    LeastPrimeFactor(3458764601677523213, 1859775391),  # semiprime
    LeastPrimeFactor(4611686018427387847, 4611686018427387847),  # prime
    LeastPrimeFactor(4611686018427387904, 2),  # 2 ** 62
    LeastPrimeFactor(4611686039902224373, 2147483647),  # semiprime
    LeastPrimeFactor(6917529027641081737, 6917529027641081737),  # prime
    LeastPrimeFactor(6917529027641081856, 2),
    LeastPrimeFactor(6917529036660811171, 2630119571),  # semiprime
    LeastPrimeFactor(9223372036854775783, 9223372036854775783),  # prime  # 2.0s on Vivobook Pro i9-11900H
    LeastPrimeFactor(9223372036854775808, 2),  # 2 ** 63
    LeastPrimeFactor(9223372037000249951, 3037000493),  # semiprime
    LeastPrimeFactor(13835058055282163681, 13835058055282163681),  # prime
    LeastPrimeFactor(13835058055282163711, 11),
    LeastPrimeFactor(13835058064511420719, 3719550773),  # semiprime
    LeastPrimeFactor(18446744030759878681, 4294967291),  # semiprime
    LeastPrimeFactor(18446744073709551557, 18446744073709551557),  # prime
    LeastPrimeFactor(18446744073709551615, 3),  # 2 ** 64 - 1
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
        assert lpf_result == exp.factor, f'wrong LPF {lpf_result} for {exp.n}'
        label = '=' if exp.prime else ' '
        print(f'{exp.n:26_d}  {label}  {exp.factor:26_d}  {elapsed:9.6f}s')
    elapsed = time.perf_counter() - t0
    print(f'{len(EXPERIMENTS)} checks in {elapsed:.2f}s')  # <5>


if __name__ == '__main__':
    auto_test()


# Timings for all 147 numbers in EXPERIMENTS:
#
# time   machine
# 9649s  RPi 4 Cortex A72
# 2564s  ThinkPad X250 i7-5600U
#  955s  Yoga 9i i7-1360P
#  791s  MacStudio M2 Max
#   78s  Vivobook Pro i9-11900H

# Timings for 18_446_744_073_709_551_557 (largest prime < 2**64)
#
# time   machine
#  833s  RPi 4 Cortex A72
#  228s  ThinkPad X250 i7-5600U
#   95s  Yoga 9i i7-1360P
#   81s  MacStudio M2 Max
#   12s  Vivobook Pro i9-11900H
