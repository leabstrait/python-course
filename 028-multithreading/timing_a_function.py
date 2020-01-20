import time

start = time.perf_counter()


def do_something():
    print('Sleeping 1 second ...')
    time.sleep(1)
    print('Done Sleeping ...')


# CPU Bound Vs. I/O Bound

do_something()  # I/O bound
do_something()  # I/O bound

finish = time.perf_counter()

print(f"Finished in {round(finish-start, 2)} second(s)")
