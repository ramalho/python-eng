"""
Interesting integers
"""

import sys


MAX_UINT64 = 18_446_744_073_709_551_615  # from Go: ^uint64(0)
assert MAX_UINT64 == 2**64 - 1

print(f'{MAX_UINT64:26d}  // max uint64')
print()
for i in range(42, 65, 2):
    n = 2**i
    print(f'{n:26d},  // 2 ** {i}')
