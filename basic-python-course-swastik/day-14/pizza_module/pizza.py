""" A module for making pizza, provides utility functions """


def make_pizza(*toppings):
    """Summarize the pizza we are about to make."""
    print("Making pizza with the following toppings: ")
    for topping in toppings:
        print('-', topping)


size_dictionary = {
    's': 'small',
    'm': 'medium',
    'l': 'large',
    'xl': 'extra-large'
}

def make_pizza_ofsize(size, *toppings):
    """Summarize the pizza we are about to make, extra information is size"""
    given_size = size.lower()
    if given_size in size_dictionary.keys():
        print(f"Making a {size_dictionary[given_size]} pizza with the following toppings: ")
        for topping in toppings:
            print('-', topping)

    else:
        print("We don't have that size")
        exit()


if __name__ == '__main__':
    make_pizza('mushroom', 'chicken', 'ham')
    make_pizza_ofsize('s', 'mushroom', 'chicken', 'ham')