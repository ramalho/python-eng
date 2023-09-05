import itertools
import time

from pathlib import Path
from multiprocessing import Event, Process

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


def spin(msg: str, completed: Event) -> None:
    for char in itertools.cycle(SPRITE):
        status = f'\r{char} {msg}'
        print(status, end='', flush=True)
        if completed.wait(.1):
            break
    blanks = ' ' * len(status)
    print(f'\r{blanks}\r', end='')


def fetch(url) -> bytes:
    resp = httpx.get(url)
    resp.raise_for_status()
    return resp.content


def download(url) -> tuple[int, str]:
    octets = fetch(url)
    name = Path(url).name
    with open(SAVE_DIR / name, 'wb') as fp:
        fp.write(octets)
    return len(octets), SAVE_DIR / name


def main():
    completed = Event()
    spinner = Process(target=spin, args=('downloading', completed))
    print(f'spinner object: {spinner}')
    spinner.start()
    url = wikipics.get_sample_url(40_000_000)
    t0 = time.perf_counter()
    size, name = download(url)
    dt = time.perf_counter() - t0
    completed.set()
    spinner.join()
    print(f'{size:_d} bytes in {dt:0.1f}s\n{name}')


if __name__ == '__main__':
    main()
