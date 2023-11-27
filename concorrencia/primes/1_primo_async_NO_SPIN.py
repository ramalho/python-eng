#!/usr/bin/env python3

# credits: Example by Luciano Ramalho inspired by
# Michele Simionato's multiprocessing example in the python-list:
# https://mail.python.org/pipermail/python-list/2009-February/675659.html

import asyncio
import itertools
import time

from primes import is_prime

async def spin(msg: str) -> None:
    for char in itertools.cycle(r'\|/-'):
        status = f'\r{char} {msg}'
        print(status, flush=True, end='')
        try:
            await asyncio.sleep(.1)
        except asyncio.CancelledError:
            break
    print('THIS WILL NEVER BE OUTPUT')


async def supervisor(n: int) -> int:
    spinner = asyncio.create_task(spin('thinking!'))  # <1>
    print(f'spinner object: {spinner}')  # <2>
    result = is_prime(n)
    spinner.cancel()  # <5>
    return result


def main() -> None:
    n = 432_345_564_227_567_561
    result = asyncio.run(supervisor(n))
    e_nao_e = 'é' if result else 'não é'
    print(n, e_nao_e, 'primo')

if __name__ == '__main__':
    main()
