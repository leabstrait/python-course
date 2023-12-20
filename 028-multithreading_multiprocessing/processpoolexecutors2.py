import concurrent.futures
import time

start = time.perf_counter()


def do_something(seconds):
    print(f'Sleeping {seconds} second ...')
    time.sleep(seconds)
    return 'Done Sleeping ...'


with concurrent.futures.ProcessPoolExecutor() as executor:
    # A list of futures
    futures = [executor.submit(do_something, 1) for _ in range(10)]
    
    # for future in futures:
    #     print(future.result())

    for future in concurrent.futures.as_completed(futures):
        print(future.result())





finish = time.perf_counter()

print(f"Finished in {round(finish-start, 2)} second(s)")
