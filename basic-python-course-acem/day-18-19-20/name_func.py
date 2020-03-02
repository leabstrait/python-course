# def get_formatted_name(first, last):
#     """Generate a neatly formatted full name."""
#     full_name = f"{first} {last}"
#     return full_name.title()

# 2: Run test for this one, should fail
# def get_formatted_name(first, last, middle): 
#     """Generate a neatly formatted full name.""" 
#     full_name = f"{first} {middle} {last}" 
#     return full_name.title()

# 3: Responding to a failing test
def get_formatted_name(first, last, middle=''): 
    """Generate a neatly formatted full name.""" 
    if middle:
        full_name = f"{first} {middle} {last}" 
    else:
        full_name = f"{first} {last}"
    return full_name.title()