def func_timer(func, *args, **kwargs):
    import time
    start = time.time()

    func(*args, **kwargs)

    end = time.time()

    return end - start


def print_name(fname, lname):
    print(fname, lname)

print(func_timer(print_name, "Labin", "Ojha"))


from recursion_fibonacci import fibo
from memoization_recursion_fibonacci import fibo as memo_fibo

print(func_timer(fibo, 8))
print(func_timer(memo_fibo, 8))
