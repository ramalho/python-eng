#!/usr/bin/env python3


'''
Download times from office rated at 140 Mbps by Fast.com

$ time ./size2secs.py 
Group 15 _____________ total _______ average
 size             96_994 B        32_331 B
 time               2.80 s          0.93 s
 rate                     34_690 B/s
Group 16 _____________ total _______ average
 size            241_158 B        80_386 B
 time               3.34 s          1.11 s
 rate                     72_130 B/s
Group 17 _____________ total _______ average
 size            439_364 B       146_455 B
 time               3.56 s          1.19 s
 rate                    123_352 B/s
Group 18 _____________ total _______ average
 size            887_113 B       295_704 B
 time               4.06 s          1.35 s
 rate                    218_399 B/s
Group 19 _____________ total _______ average
 size          1_347_667 B       449_222 B
 time               4.23 s          1.41 s
 rate                    318_652 B/s
Group 20 _____________ total _______ average
 size          3_149_093 B     1_049_698 B
 time               5.38 s          1.79 s
 rate                    584_977 B/s
Group 21 _____________ total _______ average
 size          6_191_935 B     2_063_978 B
 time               6.35 s          2.12 s
 rate                    975_415 B/s
Group 22 _____________ total _______ average
 size         12_751_287 B     4_250_429 B
 time              10.73 s          3.58 s
 rate                  1_188_022 B/s
Group 23 _____________ total _______ average
 size         23_310_838 B     7_770_279 B
 time              24.52 s          8.17 s
 rate                    950_713 B/s
Group 24 _____________ total _______ average
 size         53_967_081 B    17_989_027 B
 time              83.98 s         27.99 s
 rate                    642_621 B/s
Group 25 _____________ total _______ average
 size         95_928_637 B    31_976_212 B
 time             139.58 s         46.53 s
 rate                    687_242 B/s
Group 26 _____________ total _______ average
 size        175_464_941 B    58_488_314 B
 time             178.86 s         59.62 s
 rate                    981_028 B/s
Group 27 _____________ total _______ average
 size        340_318_067 B   113_439_356 B
 time             247.73 s         82.58 s
 rate                  1_373_720 B/s
Group 28 _____________ total _______ average
 size        802_604_257 B   267_534_752 B
 time             230.68 s         76.89 s
 rate                  3_479_370 B/s

real    1m33.293s
user    0m7.271s
sys 0m10.580s

'''

import collections
import math
from urllib import request
from urllib import parse
import pathlib
import time
import random
from concurrent import futures


BASE_URL = 'https://upload.wikimedia.org/wikipedia/commons/'
LOCAL_PATH = 'img/'
SAMPLE_LEN = 3
SIZE_INDEX = 'jpg-by-size.txt'

TimeSize = collections.namedtuple('TimeSize', 'time size')

def group_by_size():
    jpeg_by_size = collections.defaultdict(list)
    with open(SIZE_INDEX) as fp:
        for line in fp:
            size_field, path = line.strip().split()
            size = int(size_field)
            size_group = round(math.log(size, 2))
            jpeg_by_size[size_group].append(PathSize(path, size))
    return jpeg_by_size


def file_name(url):
    url_parts = parse.urlsplit(url)
    path = pathlib.PurePath(url_parts.path)
    return path.parts[-1]


def fetch(size_group, path_size: PathSize):
    url = BASE_URL + path_size.path 
    t0 = time.perf_counter()
    with request.urlopen(url) as req:
        assert req.status == 200
        octets = req.read()
        assert len(octets) == path_size.size
    dt = time.perf_counter() - t0

    name = file_name(url)
    save_path = LOCAL_PATH + name 
    with open(save_path, 'wb') as fp:
        fp.write(octets)

    return (size_group, dt, len(octets), name)


def fetch_group(size_group, path_list, executor):
    random.shuffle(path_list)
    sample = path_list[:SAMPLE_LEN]
    future_map = {}
    for path_size in sample:
        future_map[executor.submit(fetch, size_group, path_size)] = path_size
    return future_map


def main():
    jpeg_by_size = group_by_size()
    with futures.ThreadPoolExecutor() as executor:

        # submit tasks
        future_map = {}
        for size_group in jpeg_by_size:
            group_map = fetch_group(size_group, jpeg_by_size[size_group], executor)
            future_map.update(group_map)

        # get results
        group_times = collections.defaultdict(list)
        for future in futures.as_completed(future_map):
            size_group, dt, size, name = future.result()
            group = group_times[size_group]
            group.append(TimeSize(dt, size))
            if len(group) == SAMPLE_LEN:
                times, sizes = [sum(x) for x in zip(*group)]
                avg_time = times / SAMPLE_LEN
                avg_size = sizes / SAMPLE_LEN
                print(f'Group {size_group} _____________ total _______ average')
                print(f' size   \t{sizes:12_d} B\t{avg_size:12_.0f} B')
                print(f' time   \t{times:12_.2f} s\t{avg_time:12_.2f} s')
                print(f' rate   \t\t\t{sizes/times:12_.0f} B/s')


if __name__ == '__main__':
    main()
