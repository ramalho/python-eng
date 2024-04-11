import itertools
import time
from unicodedata import lookup


# ref: https://en.wikipedia.org/wiki/Braille_Patterns
DOTS = reversed((1, 2, 3, 7, 8, 6, 5, 4))
PREFIX = 'BRAILLE PATTERN DOTS-'


def girar(msg: str) -> None:
    chars = (lookup(PREFIX + str(dot)) for dot in DOTS)
    for char in itertools.cycle(chars):
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
