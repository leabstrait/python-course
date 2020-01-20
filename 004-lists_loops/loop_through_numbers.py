# Generate and Iterate through a list of numbers
for value in range(1,5):
    print(value)

# Generate a list of numbers 2 apart
for even_num in range (2, 11, 2):
    print(even_num)

# Range can be used to just create a list
even_nums = list(range(2, 11, 2))
print(even_nums)

# Create a list of squares 
list_of_squares = []

for num in range(1,11):
    square = num ** 2
    list_of_squares.append(square)
    # list_of_squares.append(num ** 2)    # A shorthand way

print(listlist_of_squares)
