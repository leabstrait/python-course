import logging

logging.basicConfig(filename='arithmetic.log',
format='%(asctime)s:%(levelname)s:%(message)s', level=logging.DEBUG)

def add(x, y):
    """Add Function"""
    return x + y

def subtract(x, y):
    """Subtract Function"""
    return x - y

def multiply(x, y):
    """Multiply Function"""
    return x * y

def divide(x, y):
    """Divide Function"""
    return x / y

a = 10.5
b = -7

add_result = add(a,b)
# print(f"Add {a} + {b} = {add_result}")
logging.debug(f"Add {a} + {b} = {add_result}")

sub_result = subtract(a,b)
# print(f"Subtract {a} - {b} = {sub_result}")
logging.debug(f"Subtract {a} - {b} = {sub_result}")

mul_result = multiply(a,b)
# print(f"Multiply {a} * {b} = {mul_result}")
logging.debug(f"Multiply {a} * {b} = {mul_result}")

div_result = divide(a,b)
# print(f"Divide {a} / {b} = {round(div_result, 2)}")
logging.debug(f"Divide {a} / {b} = {round(div_result, 2)}")

