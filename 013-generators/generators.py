# Calculates stuff as required, good for performance

def square_numbers(nums):
    for i in nums:
        yield (i * i)


sq_nums = square_numbers([1, 2, 3, 4, 5])

print(sq_nums)

print(next(sq_nums))
print(next(sq_nums))
print(next(sq_nums))
print(next(sq_nums))
print(next(sq_nums))

# print(next(sq_nums))      # Genrator StopIteration Error

# Refilling
sq_nums = square_numbers([1, 2, 3, 4, 5])
print(next(sq_nums))

# Printing as a list
print(list(sq_nums))
