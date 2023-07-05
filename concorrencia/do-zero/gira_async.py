import itertools
import asyncio
import time

async def girar(msg: str) -> None:
    for char in itertools.cycle(r'\|/-'):
        status = f'\r{char} {msg}'
        print(status, end='', flush=True)
        #if calculado.wait(0.05):
        #    break
        try:
            await asyncio.sleep(0.05)
        except asyncio.CancelledError:
            break
    blanks = ' ' * len(status)
    print(f'\r{blanks}\r', end='', flush=True)


async def calcular() -> int:
    time.sleep(3)
    return 42


async def main():
    # fio = Thread(target=girar, args=['pensando...', calculado])
    # fio.start()
    fio = asyncio.create_task(girar('pensando...'))
    res = await calcular()
    fio.cancel()
    return res


if __name__ == '__main__':
    res = asyncio.run(main())
    print(res)


