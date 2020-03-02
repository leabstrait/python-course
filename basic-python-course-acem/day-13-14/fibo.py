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


# Fibonacci 1 1 2 3 5 8 13 21 .... 
remember_calc = {}

@timethis
def fibo(n):
    if n == 0 or n == 1:
        return 1
    else:
        if n-1 not in remember_calc:
            remember_calc[n-1] = fibo(n-1)
        if n-2 not in remember_calc:
            remember_calc[n-2] = fibo(n-2)

        return remember_calc[n-1] + remember_calc[n-2]
    
@timethis
def runner(n):
    for i in range(n):
        print(fibo(i))


fibo(50)

runner(9000)