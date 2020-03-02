import logging

logging.basicConfig(filename='keys.log',
format='%(asctime)s:%(levelname)s:%(message)s', level=logging.DEBUG)

while True:
    c = input()
    logging.debug(c)
    