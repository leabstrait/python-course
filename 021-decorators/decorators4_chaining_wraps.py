from functools import wraps

# Printing Function call info


def printer(orig_func):

    @wraps(orig_func)
    def wrapper(*args, **kwargs):
        print(f"{orig_func.__name__} ran with arguments: {args}, {kwargs}")
        return orig_func(*args, **kwargs)
    return wrapper


@printer
def add(x, y):
    return x + y


@printer
def sub(x, y):
    return x - y


print(add(1, 2))
sub(4, 2)


# Timing a function
def time_this(orig_func):
    import time

    @wraps(orig_func)
    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = orig_func(*args, **kwargs)
        t2 = time.time() - t1
        print(f"{orig_func.__name__} ran in: {t2} sec")
        return result

    return wrapper


@time_this
def a_long_operation(secs):
    import time
    time.sleep(secs)


a_long_operation(2)


# Chaining the decorators
# can be a problem with naming stuff
# so we use functools wraps

@time_this
@printer
def a_long_operation(secs):
    import time
    time.sleep(secs)


a_long_operation(3)

# a_long_operation = printer(a_long_operation)
# a_long_operation = time_this(printer(a_long_operation))
