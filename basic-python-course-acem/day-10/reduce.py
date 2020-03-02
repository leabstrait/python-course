from functools import reduce


out = reduce(lambda x, y: x+y, [1,2,3,4,5,6,7,8,9,10])

print(out)


def fact(n):
    product = reduce(lambda x, y: x * y, range(1,n+1))
    return product

print(fact(5))



max = reduce(lambda x, y: x if x > y else y, [1,34,56,124,74,123])

print(max)