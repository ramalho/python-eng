from time import sleep
from unicodedata import lookup

hours = 'ONE TWO THREE FOUR FIVE SIX SEVEN EIGHT NINE TEN ELEVEN TWELVE'.split()

faces = [lookup(f'CLOCK FACE {h} OCLOCK') for h in hours]

face = 0
while True:
    now = faces[face]
    face = (face + 1) % len(faces)
    print(now, end='', flush=True)
    sleep(.1)    
    print('\r' * len(now), end='', flush=True)
