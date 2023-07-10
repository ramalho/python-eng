#!/usr/bin/env python3
from asyncio import run, get_running_loop, as_completed
import socket
from keyword import kwlist, softkwlist

MAX_KEYWORD_LEN = 10  # <1>
KEYWORDS = sorted(kwlist + softkwlist)

async def probe(domain: str) -> tuple[str, bool]:  # <2>
    loop = get_running_loop()  # <3>
    try:
        await loop.getaddrinfo(domain, None)  # <4>
    except socket.gaierror:
        return (domain, False)
    return (domain, True)


def main() -> None:  # <5>
    names = (kw for kw in KEYWORDS if len(kw) <= MAX_KEYWORD_LEN)  # <6>
    domains = (f'{name}.dev'.lower() for name in names)  # <7>
    for domain in sorted(domains):  # <9>
        domain, found = run(probe(domain))
        mark = '+' if found else ' '
        print(f'{mark} {domain}')


if __name__ == '__main__':
    main()  # <11>
