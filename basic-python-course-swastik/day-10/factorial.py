def fact(n):
    if n < 0:
        return
    elif n == 0 or n == 1:
        return 1
    else:
        return n * fact(n-1)

print(fact(-134))
print(fact(0))
print(fact(1))
print(fact(8))
