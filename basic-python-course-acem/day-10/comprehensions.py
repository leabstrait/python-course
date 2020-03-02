# squares = map(lambda x: x**2, range(1,11))
# evens = filter(lambda x: x % 2 == 0, range(1,11))

# evens = [x for x in range(1,11) if x % 2 == 0]

# alphanum = [(c, i) for c in 'abcdefghij' for i in range(1,11)]

# print(list(alphanum))


alpha = 'abcdefghi'
num = range(1,10)

# alphanum = {}
# for c, i in zip(alpha, num):
#     alphanum[c] = i



alphanum = {c: i for c, i in zip(alpha, num)}

# print(alphanum)



# my_set = {num for num in nums}

# print(nums)
# print(my_set)

nums = [1,2,3,4,5,2,5,2,6,4,6,4,3,1,2,5]


sqs = (num*num for num in nums)

print(next(sqs))
print(next(sqs))
print(next(sqs))
print(next(sqs))
print(next(sqs))
print(next(sqs))
print(next(sqs))
print(next(sqs))
print(next(sqs))
print(next(sqs))
print(next(sqs))
print(next(sqs))
print(next(sqs))
print(next(sqs))
print(next(sqs))
print(next(sqs))
print(next(sqs))
print(next(sqs))
print(next(sqs))

