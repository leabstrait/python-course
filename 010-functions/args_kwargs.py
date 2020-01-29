def get_formatted_names(*args):
    print(args)
    print(*args)

    full_name = f"{args[0]} {args[1]}"

    print(full_name.title())

get_formatted_names('Labin', 'Ojha', 26)


def get_formatted_names_kw(**kwargs):
    print(kwargs)
    print(*kwargs)

    full_name = f"{kwargs['name']} {kwargs['surname']}"

    print(full_name.title())

get_formatted_names_kw(name='Labin', surname='Ojha', age=26)