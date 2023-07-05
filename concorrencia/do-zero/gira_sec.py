import itertools
import time


def girar(msg: str) -> None:
    for char in itertools.cycle(r'\|/-'):
        status = f'\r{char} {msg}'
        print(status, end='', flush=True)
        time.sleep(0.05)


if __name__ == '__main__':
    try:
        girar('pensando para sempre...')
    except KeyboardInterrupt:
        pass
