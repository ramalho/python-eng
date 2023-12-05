# Functions to get URLs for a sample of Wikipedia
# images of an approximate byte size

import functools
import random
import bisect
from typing import TypeAlias, NamedTuple

URL: TypeAlias = str

IMG_DATA = 'jpeg-by-size.txt'
BASE_URL = 'https://upload.wikimedia.org/wikipedia/commons/'

WANTED_SIZE = 45_000_000  # bytes

class ImageDatum(NamedTuple):
    size: int
    path: str


@functools.cache
def load_img_data() -> list[ImageDatum]:
    img_data = []
    with open(IMG_DATA) as fp:
        for line in fp:
            size_str, path = line.strip().split('\t')
            size = int(size_str)
            # print(f'{size:10}\t{path}')
            img_data.append(ImageDatum(size, path))
    return img_data


def get_sample_urls(wanted_size, quantity) -> list[URL]:
    img_data = load_img_data()
    wanted = ImageDatum(wanted_size, '')
    anchor = bisect.bisect(img_data, wanted)
    # get slice 4 times bigger than quantity
    start, end = (anchor - quantity * 2), (anchor + quantity * 2)
    big_slice = img_data[start:end]
    urls = [BASE_URL + path for _, path in big_slice]
    random.shuffle(urls)
    return urls[:quantity]


def get_sample_url(wanted_size):
    return get_sample_urls(wanted_size, 20)[0]


def main():
    img_data = load_img_data()
    sample = get_sample_urls(WANTED_SIZE, 20, img_data)
    print(sample)


if __name__ == '__main__':
    main()
