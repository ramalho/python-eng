import itertools
import time
from threading import Thread, Event

def girar(msg: str, calculado: Event) -> None:
    for char in itertools.cycle(r'\|/-'):
        status = f'\r{char} {msg}'
        print(status, end='', flush=True)
        if calculado.wait(0.05):
            break
    blanks = ' ' * len(status)
    print(f'\r{blanks}\r', end='')


def calcular() -> int:
    time.sleep(3)
    return 42


def main():
    calculado = Event()
    fio = Thread(target=girar, args=['pensando...', calculado])
    fio.start()
    res = calcular()
    calculado.set()
    fio.join()
    print(res)

if __name__ == '__main__':
    main()
