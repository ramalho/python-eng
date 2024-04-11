import itertools
import time

# from threading import Thread, Event
from multiprocessing import Process, Event


def girar(msg: str, pronto: Event) -> None:
    for char in itertools.cycle(r'\|/-'):
        status = f'\r{char} {msg}'
        print(status, end='', flush=True)
        if pronto.wait(0.05):
            break
    blanks = ' ' * len(status)
    print(f'\r{blanks}\r', end='')


def buscar() -> int:
    time.sleep(3)
    return 42


def main():
    pronto = Event()
    # fio = Thread(target=girar, args=['pensando...', pronto])
    fio = Process(target=girar, args=['pensando...', pronto])
    fio.start()
    res = buscar()
    pronto.set()
    fio.join()
    print(res)


if __name__ == '__main__':
    main()
