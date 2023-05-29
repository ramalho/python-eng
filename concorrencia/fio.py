import itertools
import time
from threading import Thread, Event

from primes import is_prime

def girar(msg: str, pronto: Event) -> None:
    for char in itertools.cycle(r'\|/-'):
        status = f'\r{char} {msg}'
        print(status, end='', flush=True)
        if pronto.wait(.05):
            break
    blanks = ' ' * len(status)
    print(f'\r{blanks}\r', end='')


def supervisor():
    pronto = Event()
    girador = Thread(target=girar, args=['Computando...', pronto])
    girador.start()
    n = 7_777_777_777_777_753
    primo = is_prime(n)
    pronto.set()
    girador.join()
    e_nao_e = 'é' if primo else 'não é'
    print(n, e_nao_e, 'primo' )



if __name__ == '__main__':
    supervisor()
