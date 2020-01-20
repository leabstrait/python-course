# Decorators

# Continuation from closures
# Add functionality to existing functions using wrappers
# New Syntax

# Basic concept

# def outer_func():
#     message = 'Hi'
#     def inner_func():
#         print(message)           
#     return inner_func

# 1 Basic decoration

def decorator_function(original_function):
    def wrapper_function():
        print(f'Wrapper executed this before {original_function.__name__.title()} Function')
        return original_function()
    return wrapper_function

def display():
    print('Display Function ran')

decorated_display = decorator_function(display)
decorated_display()


# The above 4 lines can also be written as below 3 lines, @decorator systax

# @decorator_function
# def display():
#     print("Display Function ran")

# display()
