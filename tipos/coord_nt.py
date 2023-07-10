from typing import NamedTuple

class Coordinate(NamedTuple):
    lat: float                # (1)
    lon: float
    reference: str = 'WGS84'  # (2)

# experimento

sp = Coordinate(44, -23)
print(sp)
