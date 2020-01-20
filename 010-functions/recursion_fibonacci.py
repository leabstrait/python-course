def fibonacci(n):
    if n == 0:
        return
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(1))
print(fibonacci(2))
print(fibonacci(3))
print(fibonacci(4))
print(fibonacci(5))
print(fibonacci(6))


for n in range(1, 10):
    print(fibonacci(n))


# Lets try:
print(fibonacci(37))