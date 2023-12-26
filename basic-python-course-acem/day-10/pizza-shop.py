import sys

print(sys.path)
sys.path.append('pizzamake')
print(sys.path)


from pizza import *

# print(pizza.__name__)


print("The shop is open")

print("Send your order")

make_pizza("Mushroom", "chicken", "pork")
make_pizza_ofsize(14, "Mushroom", "chicken", "pork")