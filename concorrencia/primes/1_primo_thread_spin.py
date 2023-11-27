#!/usr/bin/env python3

import itertools
from threading import Thread, Event

from primes import is_prime


def girar(msg: str, pronto: Event) -> None:
    for char in itertools.cycle(r'\|/-'):
        status = f'\r{char} {msg}'
        print(status, end='', flush=True)
        if pronto.wait(0.05):
            break
    blanks = ' ' * len(status)
    print(f'\r{blanks}\r', end='')


def main():
    pronto = Event()
    girador = Thread(target=girar, args=['Computando...', pronto])
    girador.start()
    n = 432_345_564_227_567_561
    primo = is_prime(n)
    pronto.set()
    girador.join()
    e_nao_e = 'é' if primo else 'não é'
    print(n, e_nao_e, 'primo')


if __name__ == '__main__':
    main()
