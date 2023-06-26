#!/usr/bin/env python3
from asyncio import run, get_running_loop, as_completed
import socket
from keyword import kwlist, softkwlist

MAX_KEYWORD_LEN = 5  # <1>
KEYWORDS = sorted(kwlist + softkwlist)

async def probe(domain: str) -> tuple[str, bool]:  # <2>
    loop = get_running_loop()  # <3>
    try:
        await loop.getaddrinfo(domain, None)  # <4>
    except socket.gaierror:
        return (domain, False)
    return (domain, True)

async def main() -> None:  # <5>
    names = (kw for kw in KEYWORDS if len(kw) <= MAX_KEYWORD_LEN)  # <6>
    domains = (f'{name}.dev'.lower() for name in names)  # <7>
    coros = [probe(domain) for domain in domains]  # <8>
    for coro in as_completed(coros):  # <9>
        domain, found = await coro  # <10>
        mark = '+' if found else ' '
        print(f'{mark} {domain}')


if __name__ == '__main__':
    run(main())  # <11>
