import itertools
import asyncio
import time


async def girar(msg: str) -> None:
    for char in itertools.cycle(r'\|/-'):
        status = f'{char} {msg}'
        print(status, end='\r', flush=True)
        # if calculado.wait(0.05):
        #    break
        try:
            await asyncio.sleep(0.05)
        except asyncio.CancelledError:
            break
    blanks = ' ' * len(status)
    print(f'\r{blanks}\r', end='', flush=True)


async def buscar() -> int:
    await asyncio.sleep(3)
    return 42


async def main():
    # girador = Thread(target=girar, args=['pensando...', calculado])
    girador = asyncio.create_task(girar('pensando...'))
    # girador.start()
    res = await buscar()
    girador.cancel()
    return res


if __name__ == '__main__':
    res = asyncio.run(main())
    print('Resposta:', res)
