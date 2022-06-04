import asyncio


async def f(i: int):
    print(f'i={i}, f()')
    # await asyncio.sleep(1)
    import time
    time.sleep(1)

    print(f'i={i}, f() slept')
    return i * 3


async def g(i: int):
    # ============================
    # code block 1
    # g() runs the code here like normal
    a = i * 2

    print(f'i={i}, code block=1')
    # ============================

    r = await f(i)  # g() actually pause execution after calling f()

    # ============================
    # code block 2
    # g() runs the code here after f() finishes
    print(f'i={i}, code block=2')
    b = i * 4
    return a, b, r
    # ============================


async def main():
    await asyncio.gather(g(1), g(2), g(3))


if __name__ == '__main__':
    asyncio.run(main())
