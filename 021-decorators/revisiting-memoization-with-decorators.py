# Implement this decorator later
def memoizer(func):
    memory = {}
    def wrapper(n):
        if n not in memory:
            memory[n] = func(n)
        return memory[n]
    return wrapper

@memoizer
def fibonacci(n):
    if n == 0:
        return
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

for n in range(1, 10):
    print(fibonacci(n))

# Lets try:
print(fibonacci(35))


