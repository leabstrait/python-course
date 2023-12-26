import sys

sys.path.append('pizza_module')

from pizza import *
import os


make_pizza('mushroom', 'chicken', 'ham')
make_pizza_ofsize('m', 'mushroom', 'chicken', 'ham')
print(size_dictionary)