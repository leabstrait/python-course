class MyRange:

    def __init__(self, start, end):
        self.value = start
        self.end = end

    def __iter__(self):
        return self
        # __iter__ returns an iterator which will need to define a __next__ method, done below

    def __next__(self):
        if self.value >= self.end:
            raise StopIteration

        current = self.value
        self.value += 1
        return current

nums = MyRange(1, 10)

for num in nums:
    print(num)


# Generators are iterators as well

def my_range(start, end):
    current = start
    while current < end:
        yield current
        current += 1

nums = my_range(1, 10)

for num in nums:
    print(num)

# Iterators can be infinite as well
def my__infinite_range(start):
    current = start
    while True:
        yield current
        current += 1

nums = my__infinite_range(1)

print(next(nums))
print(next(nums))
print(next(nums))
print(next(nums))
print(next(nums))
print(next(nums))
print(next(nums))
print(next(nums))
print(next(nums))
print(next(nums))
print(next(nums))
print(next(nums))
print(next(nums))
print(next(nums))
print(next(nums))
print(next(nums))
print(next(nums))