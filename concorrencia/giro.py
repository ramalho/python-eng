import itertools
import time

def girar(msg: str) -> None:
    for char in itertools.cycle(r'\|/-'):
        status = f'\r{char} {msg}'
        print(status, end='', flush=True)
        time.sleep(.05)
    blanks = ' ' * len(status)
    print(f'\r{blanks}\r', end='')


if __name__ == '__main__':
    try:
        girar('pensando...')
    except KeyboardInterrupt:
        pass
