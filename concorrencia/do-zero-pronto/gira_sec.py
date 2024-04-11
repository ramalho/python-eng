import itertools
import time


def girar(msg: str) -> None:
    for char in itertools.cycle(r'\|/-'):
        status = f'\r{char} {msg}'
        print(status, end='', flush=True)
        time.sleep(0.1)


def main() -> None:
    try:
        girar('pensando para sempre...')
    except KeyboardInterrupt:
        pass


if __name__ == '__main__':
    main()
