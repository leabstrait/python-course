remember_fib = {}


def fibonacci(n):
    if n == 0:
        return
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        if n-1 not in remember_fib:
            remember_fib[n-1] = fibonacci(n-1)
        if n-2 not in remember_fib:
            remember_fib[n-2] = fibonacci(n-2)
        
        return remember_fib[n-1] + remember_fib[n-2]


for n in range(1, 10):
    print(fibonacci(n))


# Lets try:
print(fibonacci(100))
