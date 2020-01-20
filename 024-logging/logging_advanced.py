import logging

# Set logger Name
logger = logging.getLogger(__name__)
# Set logging Level
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s:%(name)s:%(message)s')

file_handler = logging.FileHandler('advanced_test.log')
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)

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


num_1 = 20
num_2 = 5

add_result = add(num_1, num_2)
# print(f"Add: {num_1} + {num_2} = {add_result}")
logger.debug(f"Add: {num_1} + {num_2} = {add_result}")


sub_result = subtract(num_1, num_2)
# print(f"Subtract: {num_1} - {num_2} = {sub_result}")
logger.debug(f"Subtract: {num_1} - {num_2} = {sub_result}")


mul_result = multiply(num_1, num_2)
# print(f"Multiply: {num_1} x {num_2} = {mul_result}")
logger.debug(f"Multiply: {num_1} x {num_2} = {mul_result}")


div_result = divide(num_1, num_2)
# print(f"Divide: {num_1} / {num_2} = {div_result}")
logger.debug(f"Divide: {num_1} / {num_2} = {div_result}")
