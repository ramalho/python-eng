from collections.abc import Iterable, AsyncIterator
from typing import NamedTuple

import asyncio
import socket


class Result(NamedTuple):  # <1>
    domain: str
    found: bool


async def probe(domain: str, loop: asyncio.AbstractEventLoop) -> Result:  # <3>
    try:
        await loop.getaddrinfo(domain, None)
    except socket.gaierror:
        return Result(domain, False)
    return Result(domain, True)


async def multi_probe(domains: Iterable[str]) -> AsyncIterator[Result]:  # <4>
    loop = asyncio.get_running_loop()
    coros = [probe(domain, loop) for domain in domains]  # <5>
    for coro in asyncio.as_completed(coros):  # <6>
        result = await coro  # <7>
        yield result  # <8>
