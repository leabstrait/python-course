import time

def time_this(given_function):

    def timing_wrapper(*args, **kwargs):

        start_time = time.time()
        result = given_function(*args, **kwargs)
        end_time = time.time()
        time_taken = end_time - start_time
        print(f"{given_function.__name__} ran in: {time_taken} secs.")
        return result

    return timing_wrapper

@time_this
def a_long_operation(secs):
    print(f"A long operation started, will pause for {secs} seconds")
    time.sleep(secs)
    print("A long operation ended")

timed_a_long_operation = time_this(a_long_operation)

# timed_a_long_operation(2)
# timed_a_long_operation(2)
# timed_a_long_operation(2)

a_long_operation(0)
a_long_operation(5)
a_long_operation(10)
