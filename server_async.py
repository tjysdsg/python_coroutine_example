import asyncio
import time

N_WORKERS = 100


async def worker(worker_id: int):
    print(f"{worker_id}: receiving data 1")
    await asyncio.sleep(1)

    print(f"{worker_id}: receiving data 2")
    await asyncio.sleep(0.5)

    print(f"{worker_id}: receiving data 3")
    await asyncio.sleep(1)

    print(f"{worker_id}: sending data 4")
    await asyncio.sleep(1.5)


async def main():
    await asyncio.gather(*[worker(i) for i in range(N_WORKERS)])


if __name__ == '__main__':
    s = time.perf_counter()
    asyncio.run(main())
    elapsed = time.perf_counter() - s
    print(f"{elapsed:0.2f} seconds.")
