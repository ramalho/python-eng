import itertools
import time

SPRITE = r'\|/-'

# https://en.wikipedia.org/wiki/Braille_Patterns
SPRITE = [
    '\N{BRAILLE PATTERN DOTS-14}',
    '\N{BRAILLE PATTERN DOTS-25}',
    '\N{BRAILLE PATTERN DOTS-36}',
    '\N{BRAILLE PATTERN DOTS-78}',
]


def spin(msg: str) -> None:
    for char in itertools.cycle(SPRITE):
        status = f'\r{char} {msg}'
        print(status, end='', flush=True)
        time.sleep(0.1)
    blanks = ' ' * len(status)
    print(f'\r{blanks}\r', end='')


if __name__ == '__main__':
    try:
        spin('thinking...')
    except KeyboardInterrupt:
        pass
