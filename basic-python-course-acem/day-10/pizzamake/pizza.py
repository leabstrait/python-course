"""Module for making pizza"""

def make_pizza(*toppings):
    """Make a piza with supplied toppings"""
    print("\nMaking a pizza with the following toppings:")
    for topping in toppings:
        print(f" - {topping}")



def make_pizza_ofsize(size, *toppings):
    """Make a piza with supplied toppings of given size"""
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f" - {topping}")


if __name__ == '__main__':
    make_pizza("Mushroom", "chicken", "pork")
    make_pizza_ofsize(14, "Mushroom", "chicken", "pork")