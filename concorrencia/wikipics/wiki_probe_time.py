#!/usr/bin/env python3

# Measure download times to find image size that
# takes approximately TARGET seconds to download.

import math
import time

import httpx

import wikipics


TARGET = 3.5  # seconds of download time
TOLERANCE = 0.2  # relative tolerance

MEGABYTES = 1024 * 1024


def fetch(url) -> bytes:
    resp = httpx.get(url, timeout=TARGET * 3)
    resp.raise_for_status()
    return resp.content


def new_guess(lower: int, upper: int) -> int:
    offset = (upper - lower) // 2
    return lower + offset


def probe(target: float, img_data: tuple[int, str]) -> int:
    lower = 0
    upper = len(img_data)
    while True:
        guess = new_guess(lower, upper)
        size, path = img_data[guess]
        print(
            f'[{guess}] {size/MEGABYTES:_.1f} MB: {path} ', flush=True, end=''
        )
        t0 = time.perf_counter()
        content = fetch(wikipics.BASE_URL + path)
        dt = time.perf_counter() - t0
        print(f'{dt:0.2f}s')
        assert len(content) == size
        if math.isclose(target, dt, rel_tol=TOLERANCE):
            return (guess, dt)
        if dt < target:
            lower = guess
        else:
            upper = guess


def main():
    img_data = wikipics.load_img_data()
    guess, dt = probe(TARGET, img_data)
    size, _ = img_data[guess]
    print(
        f'{dt:0.2f}s for image sized {size:_d} B at index [{guess}] of {len(img_data)}.'
    )


if __name__ == '__main__':
    main()
