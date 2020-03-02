from functools import reduce

out= reduce(lambda x, y: x + y, [1,2,3,4,5,6,7,8,9,10])

out = reduce(lambda x, y: x if x > y else y, [1,4,6,23,623,72,78,723,6])

print(out)




