import time

def timethis(fn):
    def calc_time_wrapper(*args, **kwargs):
        print(f"Function {fn.__name__} running with {args} and {kwargs}")
        start = time.time()
        result = fn(*args, **kwargs)
        end = time.time()
        print(f"the function required {end - start} seconds.")
        return result

    return calc_time_wrapper


@timethis
def sleeper(sleepforsec=1):
    time.sleep(sleepforsec)

@timethis
def add(x,y,a=5):
    return x+y+a



# sleeper()
# sleeper(sleepforsec=4)
print(add(3,5))
print(add(3,5,7))
print(add(3,5,a=9))