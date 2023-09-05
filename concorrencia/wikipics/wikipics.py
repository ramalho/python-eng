# Functions to get URLs for a sample of Wikipedia
# images of an approximate byte size

from bisect import bisect
from typing import TypeAlias

import random

URL: TypeAlias = str

IMG_DATA = 'jpeg-by-size.txt'
BASE_URL = 'https://upload.wikimedia.org/wikipedia/commons/'

TARGET_SIZE = 45_000_000  # bytes


def load_img_data() -> list[tuple[int, str]]:
    img_data = []
    with open(IMG_DATA) as fp:
        for line in fp:
            size_str, path = line.strip().split('\t')
            size = int(size_str)
            # print(f'{size:10}\t{path}')
            img_data.append((size, path))
    return img_data


def get_sample_urls(wanted_size, quantity, img_data=None) -> list[URL]:
    if img_data is None:
        img_data = load_img_data()
    wanted = (wanted_size, '')
    anchor = bisect(img_data, wanted)
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
    sample = get_sample_urls(TARGET_SIZE, 20, img_data)
    print(sample)


if __name__ == '__main__':
    main()
