# later import individual fn from pizza
# also import as p
# also import all *
import sys
sys.path.append('pizza')

from pizza import make_pizza

def make_pizza(*toppings):
    """Summarize the pizza we are about to make."""
    print("\nMaking a pizza with the following toppings:") 
    for topping in toppings: 
        print(f"- {topping}") 
        
make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')
