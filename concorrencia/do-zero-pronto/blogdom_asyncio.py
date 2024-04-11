#!/usr/bin/env python3
import asyncio
import socket
from keyword import kwlist, softkwlist

MAX_KEYWORD_LEN = 5
NAMES = [kw for kw in kwlist+softkwlist if len(kw) <= MAX_KEYWORD_LEN]


async def probe(domain: str) -> tuple[str, bool]:
    try:
        await asyncio.get_running_loop().getaddrinfo(domain, None)
    except socket.gaierror:
        return (domain, False)
    return (domain, True)


async def main():
    domains = (f'{name}.dev'.lower() for name in NAMES)
    coros = [probe(domain) for domain in domains]  # (8)
    for coro in asyncio.as_completed(coros):  # (9)
        domain, found = await coro  # (10)
        mark = '+' if found else ' '
        print(f'{mark} {domain}')


if __name__ == '__main__':
    asyncio.run(main())
