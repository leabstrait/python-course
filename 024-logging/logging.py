import logging

# DEBUG: Detailed information, typically of interest only when diagnosing problems.

# INFO: Confirmation that things are working as expected.

# (default)
# WARNING: An indication that something unexpected happened, or indicative of some problem in the near future (e.g. ‘disk space low’). The software is still working as expected.

# ERROR: Due to a more serious problem, the software has not been able to perform some function.

# CRITICAL: A serious error, indicating that the program itself may be unable to continue running.

# Set log level, logfile, log format
logging.basicConfig(filename='test.log', 
format='%(asctime)s:%(levelname)s:%(message)s',level=logging.DEBUG)
# logging to a file is an appending operation

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
logging.debug(f"Add: {num_1} + {num_2} = {add_result}")


sub_result = subtract(num_1, num_2)
# print(f"Subtract: {num_1} - {num_2} = {sub_result}")
logging.debug(f"Subtract: {num_1} - {num_2} = {sub_result}")


mul_result = multiply(num_1, num_2)
# print(f"Multiply: {num_1} x {num_2} = {mul_result}")
logging.debug(f"Multiply: {num_1} x {num_2} = {mul_result}")


div_result = divide(num_1, num_2)
# print(f"Divide: {num_1} / {num_2} = {div_result}")
logging.debug(f"Divide: {num_1} / {num_2} = {div_result}")
