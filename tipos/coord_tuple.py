from geolib import geohash as gh  # type: ignore  # (1)

PRECISION = 9

def geohash(lat_lon: tuple[float, float]) -> str:  # (2)
    return gh.encode(*lat_lon, PRECISION)

