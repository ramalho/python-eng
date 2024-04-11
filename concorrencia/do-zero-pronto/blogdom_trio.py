#!/usr/bin/env python3
import trio
import trio.socket as socket
from trio.abc import SendChannel, ReceiveChannel
from keyword import kwlist, softkwlist

MAX_KEYWORD_LEN = 5
NAMES = [kw for kw in kwlist+softkwlist if len(kw) <= MAX_KEYWORD_LEN]


async def probe(sender: SendChannel, domain: str):
    async with sender:
        try:
            await socket.getaddrinfo(domain, None)
            result = (domain, True)
        except socket.gaierror:
            result = (domain, False)
        await sender.send(result)


async def report(receiver: ReceiveChannel):
    async with receiver:
        async for domain, found in receiver:
            mark = '+' if found else '-'
            print(f'{mark} {domain}')


async def main():
    domains = [f'{name}.dev'.lower() for name in NAMES]
    sender, receiver = trio.open_memory_channel(0)

    async with trio.open_nursery() as nursery:
        async with sender:
            for domain in domains:
                nursery.start_soon(probe, sender.clone(), domain)

        nursery.start_soon(report, receiver)


if __name__ == '__main__':
    trio.run(main)
