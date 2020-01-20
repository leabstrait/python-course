# Closures

# A closure is an inner function that remembers and has access
# to variables in the local scope that it was created even when
# the outer function has finished executing


# 1 return inner_func after executing

# def outer_func():
#     message = 'Hi'

#     def inner_func():
#         # message is a free variable inside this function since it's not defined here
#         print(message)           

#     return inner_func()

# outer_func()

# 2 return the inner_func without executing

# def outer_func():
#     message = 'Hi'

#     def inner_func():
#         # message is a free variable inside this function since it's not defined here
#         print(message)           

#     return inner_func

# myfunc = outer_func()
# # What is myfunc
# print(myfunc)
# # Run it
# # We see that the variable from enclosing scope was preserved
# myfunc()

# 3 Also works with parameters

# def outer_func(msg):
#     message = msg

#     def inner_func():
#         # message is a free variable inside this function since it's not defined here
#         print(message)           

#     return inner_func

# hifunc = outer_func('Hi')
# byefunc = outer_func('Bye')

# hifunc()
# byefunc()

# 4 A practical example

def printer(func):
    def print_func(*args):
        print(f"Running '{func.__name__}' with arguments: {args}")
        print("Result:", func(*args))
    return print_func

def add(x, y):
    return x + y

def sub(x, y):
    return x -y

add_printer = printer(add)
sub_printer = printer(sub)

add_printer(3, 5)
sub_printer(9, 7)


