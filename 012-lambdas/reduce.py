from functools import reduce


out = reduce(lambda x, y: x + y, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(out)


# Factorial

fact = reduce(lambda x, y: x * y, [5, 4, 3, 2, 1])
print(fact)


# Find max

max = reduce(lambda x, y: x if x > y else y, [4,5,2,7,1,8,2,9,2])
print(max)