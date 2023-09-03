#!/usr/bin/env python3

import re
from urllib.parse import urlparse
import http.client
import os
import threading

# src="//upload.wikimedia.org/wikipedia/commons/thumb/b/ba/MachuPichuSacredValley_fir000202_edit.jpg/500px-MachuPichuSacredValley_fir000202_edit.jpg

BASE_URL = 'https://upload.wikimedia.org/wikipedia/commons/'  #… b/ba/MachuPichuSacredValley_fir000202_edit.jpg'

THUMB_RE = re.compile(r'src="//upload.wikimedia.org/wikipedia/commons/thumb/(\w)/(\w\w)/([^/]+)')

HTML_DIR = 'html'
PIC_DIR = 'img'


class DownloadError(OSError):

    def __init__(self, msg):
        super().__init__()
        self.msg = msg

    def __repr__(self):
        return f'DownloadError({self.msg!r})'


def pic_paths(year, month):
    with open(f'{HTML_DIR}/{year}-{month:02d}.html') as fp:
        html = fp.read()
    for match in THUMB_RE.findall(html):
        md5_prefix = '/'.join(match[:2])
        yield md5_prefix, match[2]


def get_pic(cnx, path, month_dir, name):
    full_name = month_dir + '/' + name
    print(full_name)
    cnx.request('GET', path)
    resp = cnx.getresponse()
    assert resp.status == 200, f'{resp.status}, {resp.reason}'
    try:
        body = resp.read()
    except http.client.IncompleteRead as exc:
        raise DownloadError(full_name) from exc
    with open(full_name, 'wb') as fp:
        fp.write(body)


def get_month(year, month):
    url = urlparse(BASE_URL)
    cnx = http.client.HTTPSConnection(url.netloc)

    month_dir = f'{PIC_DIR}/{year}/{month:02d}'
    os.makedirs(month_dir, exist_ok=True)

    for md5_prefix, name in pic_paths(year, month):
        path = '/'.join([url.path, md5_prefix, name])
        get_pic(cnx, path, month_dir, name)

    cnx.close()


def get_year(year):
    threads = []

    for month in range(1, 13):
        t = threading.Thread(target=get_month, args=(year, month))
        t.start()
        threads.append(t)

    for thread in threads:
        thread.join()

for year in range(2006, 2007):
    get_year(year)

