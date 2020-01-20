# Class Decorators

# The decorator function

# def decorator_function(original_function):
#     def wrapper_function(*args, **kwargs):
#         print(f'Wrapper executed this before {original_function.__name__.title()} Function')
#         return original_function(*args, **kwargs)
#     return wrapper_function


class decorator_class(object):

    def __init__(self, original_function):
        self.original_function = original_function

    def __call__(self, *args, **kwargs):
        print(f"call method executed this before {self.original_function.__name__}")
        return self.original_function(*args, **kwargs)


# Use our decorator_class to decorate our previous functions
@decorator_class
def display():
    print("Display Function ran")

@decorator_class
def display_person(name, age):
    print(f"display_person ran with arguments ({name}, {age})")


display()
display_person('Labin', 26) 