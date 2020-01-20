# Decorators with arguments

def decorator_param(n_times):
    def decorator_function(original_function):
        def wrapper_function(*args, **kwargs):
            print(f'Wrapper executed this before {original_function.__name__.title()} Function')
            for _ in range(0, n_times):
                original_function(*args, **kwargs)
            return
        return wrapper_function
    return decorator_function


@decorator_param(5)
def display(name, age):
    print(f"Display Function ran with arguments {name}, {age}")

display('Labin', 26)