#!/usr/bin/env python3

"""
Interesting integers for experiments
"""

import sys


MAX_UINT64 = 18_446_744_073_709_551_615  # from Go: ^uint64(0)
assert MAX_UINT64 == 2**64 - 1

print(f'{MAX_UINT64:26d}  // max uint64')
print()
for i, j in enumerate(range(29, 65, 5), 1):
    n = 2**j
    # print(f'{i:2d}', end = ' ')
    print(f'{n:26d},  // 2 ** {j}')
