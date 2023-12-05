#!/usr/bin/env python3

import asyncio
import itertools
import time

from pathlib import Path

import httpx

import wikipics

SAVE_DIR = Path('img')

# https://en.wikipedia.org/wiki/Braille_Patterns
SPRITE = [
    '\N{BRAILLE PATTERN DOTS-14}',
    '\N{BRAILLE PATTERN DOTS-25}',
    '\N{BRAILLE PATTERN DOTS-36}',
    '\N{BRAILLE PATTERN DOTS-78}',
]


async def spin(msg: str) -> None:
    for char in itertools.cycle(SPRITE):
        status = f'\r{char} {msg}'
        print(status, end='', flush=True)
        try:
            await asyncio.sleep(0.1)
        except asyncio.CancelledError:
            break
    blanks = ' ' * len(status)
    print(f'\r{blanks}\r', end='', flush=True)


async def fetch(url) -> bytes:
    async with httpx.AsyncClient() as client:
        resp = await client.get(url)
        resp.raise_for_status()
        return resp.content


async def download(url) -> tuple[int, str]:
    octets = await fetch(url)
    name = Path(url).name
    with open(SAVE_DIR / name, 'wb') as fp:
        fp.write(octets)
    return len(octets), SAVE_DIR / name


async def supervisor() -> str:
    spinner = asyncio.create_task(spin('downloading'))
    print(f'spinner object: {spinner}')
    url = wikipics.get_sample_url(40_000_000)
    t0 = time.perf_counter()
    size, name = await download(url)
    dt = time.perf_counter() - t0
    spinner.cancel()
    return f'{size:_d} bytes in {dt:0.1f}s\n{name}'


def main():
    msg = asyncio.run(supervisor())
    print(msg)


if __name__ == '__main__':
    main()
