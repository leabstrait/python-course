def sqs(nums):
    for num in nums:
        yield(num*num)


sq = sqs([1,2,3,4,5])

# print(next(sq))
# print(next(sq))
# print(next(sq))
# print(next(sq))
# print(next(sq))
# print(next(sq))


for s in sq:
    print(s)