def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = f"{first_name} {last_name}"
    return full_name.title()


labin = get_formatted_name('Labin', 'Ojha')
print(musician)


def get_formatted_name_2(first_name, last_name, middle_name=''):
    """Return a full name, neatly formatted."""
    full_name = f"{first_name} {middle_name} {last_name}"
    return full_name.title()


someone_in_class = get_formatted_name('a', 'b', 'c')
someone_in_class_2 = get_formatted_name('a', 'b', 'c')
print(someone_in_class)
print(someone_in_class_2)


def build_person(first_name, last_name, age):
    """Return a dictionary of information about a person."""
    person = {'first': first_name,
            'last': last_name,
            'age': age}
    return person

labin_info = build_person('labin', 'ojha', 26)
print(labin_info)

