nums = [1,2,3,4,5,6,7,8,9]

def square_gen_func(nums):
    for n in nums:
        yield n*n

sq_gen = square_gen_func(nums)

# print(list(sq_gen))

# for sq in sq_gen:
#     print(sq)

# Using a comprehension

sq_gen = (num*num for num in nums)

print(list(sq_gen))

for sq in sq_gen:
    print(sq)
