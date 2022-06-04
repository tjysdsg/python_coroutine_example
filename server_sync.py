import time

N_WORKERS = 100


def worker(worker_id: int):
    print(f"{worker_id}: receiving data 1")
    time.sleep(1)

    print(f"{worker_id}: receiving data 2")
    time.sleep(0.5)

    print(f"{worker_id}: receiving data 3")
    time.sleep(1)

    print(f"{worker_id}: sending data 4")
    time.sleep(1.5)


def main():
    [worker(i) for i in range(N_WORKERS)]


if __name__ == '__main__':
    s = time.perf_counter()
    main()
    elapsed = time.perf_counter() - s
    print(f"{elapsed:0.2f} seconds.")
