def make_pizza(*toppings):
    """Summarize the pizza we are about to make."""
    print("\nMaking a pizza with the following toppings:") 
    for topping in toppings: 
        print(f"- {topping}") 

def make_pizza_ofsize(size, *toppings):
    """Summarize the pizza we are about to make."""
    print(f"\nMaking a {size}-inch pizza with the following toppings:") 
    for topping in toppings: 
        print(f"- {topping}") 
        

print(__name__)
if __name__ == '__main__':        
            
    make_pizza('chicken') 
    make_pizza('mushrooms', 'green peppers', 'extra cheese')

    make_pizza_ofsize(16, 'chicken') 
    make_pizza_ofsize(12, 'mushrooms', 'green peppers', 'extra cheese')

# Run in interpreter first
# import pizza
