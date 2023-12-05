#!/usr/bin/env python3

"""
Demo: download images with concurrent.futures
"""

from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
import time

import httpx

import wikipics

WANTED_SIZE = 10 * 2 ** 20  # 40 MB
SAMPLE_LEN = 20
SAVE_DIR = Path('img')

def save(filename: str, data: bytes):
    if len(filename) > 255:  # common OS limit
        filename = filename[:255]
    with open(filename, 'wb') as fp:
        fp.write(data)

def download(url) -> tuple[wikipics.ImageDatum, float]:
    t0 = time.perf_counter()
    resp = httpx.get(url)
    resp.raise_for_status()
    name = Path(url).name
    save(str(SAVE_DIR / name), resp.content)
    elapsed = time.perf_counter() - t0
    img = wikipics.ImageDatum(len(resp.content), str(SAVE_DIR / name))
    return (elapsed, img)


def crop_path(path: str, max_len:int=65) -> str:
    if len(path) > max_len:
        return path[:max_len - 1] + '\N{HORIZONTAL ELLIPSIS}'
    return path


def main():
    sample = wikipics.get_sample_urls(WANTED_SIZE, SAMPLE_LEN)
    t0 = time.perf_counter()
    processing_time = 0
    qtd_threads = 0
    success_count = 0

    with ThreadPoolExecutor() as executor:
        # Submit the download tasks to the executor
        futures = [executor.submit(download, url) for url in sample]
        qtd_threads = executor._max_workers
        print(f'Downloading {len(futures)} images with up to {qtd_threads} threads')

        # Wait for the tasks to complete
        for future in as_completed(futures): # , timeout=10
            # Get the result of the task
            try:
                elapsed, img = future.result()
            except httpx.HTTPStatusError as exc:
                print(f'HTTP error {exc}')
                continue
            success_count += 1
            path = crop_path(img.path)
            print(f'[{elapsed:3.1f}s] {img.size:10_d}  {path}')
            processing_time += elapsed
    elapsed = time.perf_counter() - t0
    print(f'{success_count} downloads in {elapsed:.1f}s')
    print(f'Total processing time: {processing_time:.1f}s using {qtd_threads} threads.')



if __name__ == '__main__':
    main()