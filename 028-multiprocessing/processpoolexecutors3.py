import concurrent.futures
import time

start = time.perf_counter()


def do_something(seconds):
    print(f'Sleeping {seconds} second ...')
    time.sleep(seconds)
    return f'Done Sleeping ... {seconds}'


with concurrent.futures.ProcessPoolExecutor() as executor:
    # Passing functions with variable execution time
    
    secs = [5,4,3,2,1]
    # futures = [executor.submit(do_something, sec) for sec in secs]
    
    # Built-in way for above case
    results = executor.map(do_something, secs)

    # for future in concurrent.futures.as_completed(futures):
    #     print(future.result())

    # Map return the result, hence
    for result in results:
        print(result)

finish = time.perf_counter()

print(f"Finished in {round(finish-start, 2)} second(s)")
