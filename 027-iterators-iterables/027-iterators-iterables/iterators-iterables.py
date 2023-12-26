nums = [1,2,3]

for num in nums:
    print(num)

print(dir(list))

# needs __iter__ method for iterator
# list is an iterable but not an iterator
# implementing __iter__ returns an iterator
# iterators also have a __next__ method, which list doesn't

i_nums = nums.__iter__()
# or
i_nums = iter(nums)

print(i_nums)
print(dir(i_nums))

# print(next(i_nums))
# print(next(i_nums))
# print(next(i_nums))
# # print(next(i_nums))

while True:
    try:
        item = next(i_nums)
        print(item)
    except StopIteration:
        break
