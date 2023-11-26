#!/usr/bin/env python3

import itertools
import time
from typing import NoReturn

SPRITE = r'\|/-'


def spin(msg: str) -> NoReturn:
    try:
        for char in itertools.cycle(SPRITE):
            status = f'\r{char} {msg}'
            print(status, end='', flush=True)
            time.sleep(0.1)
    except KeyboardInterrupt:
        blanks = ' ' * len(status)
        print(f'\r{blanks}\r', end='')


if __name__ == '__main__':
    spin('thinking forever...')
