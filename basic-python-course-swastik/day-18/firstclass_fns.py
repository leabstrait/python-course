# First Class Functions
# Meaning: For functions to be treated as first class they must be
# able to be passed as an argument, returned from a function, and
# assigned to a variable, which is generally available to other
# entities in the proglang.


# 1 Assigning functions to variables

def square(x):
    return x*x


print(square(4))

power_2 = lambda x: x*x

print(power_2(4))


# 2 Passing functions as parameters

def cube(x):
    return x*x*x

def my_map(func, my_list):
    result = []
    for elem in my_list:
        result.append(func(elem))
    return result

squares = my_map(square, [1, 2, 3, 4, 5, 6, 7])
print(squares)

cubes = my_map(cube, [1, 2, 3, 4, 5, 6, 7])
print(cubes)

# Return a function: see closures

import return_functions


return_functions.__name__