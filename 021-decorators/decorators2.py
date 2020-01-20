# Decorators on functions that take arguments
def decorator_function(original_function):
    def wrapper_function(*args, **kwargs):
        print(f'Wrapper executed this before {original_function.__name__.title()} Function')
        return original_function(*args, **kwargs)
    return wrapper_function

# Add the decorator to the previous function
@decorator_function
def display():
    print("Display Function ran")


# Add above decorator to yet another function
@decorator_function
def display_person(name, age):
    print(f"display_person ran with arguments ({name}, {age})")


display()
display_person('Labin', 26) 

