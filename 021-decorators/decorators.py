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
    def wrapper_function(*args, **kwargs):
        print(f'Wrapper executed this before {original_function.__name__.title()} Function')
        original_function(*args, **kwargs)
        print(f'Wrapper executed this after {original_function.__name__.title()} Function')
        
    return wrapper_function

def display(*args, **kwargs):
    print('Display Function ran')
    print(args, kwargs)


decorated_display = decorator_function(display)
decorated_display(1,2,3,4, name="Badri", surname='Aran')


# The above 4 lines can also be written as below 3 lines, @decorator systax

# @decorator_function
# def display():
#     print("Display Function ran")

# display()
