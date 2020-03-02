def get_formatted_names(*args):
    print(args)
    print(*args)

    full_name = f"My name is {args[0]} {args[1]}"

    print(full_name.title())

    print(f"I am {args[2]} years old")

# get_formatted_names('Labin', 'Ojha', 26)









def get_formatted_names_kw(**kwargs):
    print(kwargs)
    print(*kwargs)
    print(**kwargs)
    print(name='Labin', surname='Ojha', age=26)

    full_name = f"My name is {kwargs['name']} {kwargs['surname']}"

    print(full_name.title())

    print(f"I am {kwargs['age']} years old")

get_formatted_names_kw(name='Labin', surname='Ojha', age=26)