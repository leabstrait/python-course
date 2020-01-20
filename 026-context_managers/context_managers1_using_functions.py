# Context Managers:
# Use Cases:
#     - Close off files after use
#     - Close connection to databases automatically
#     - Acquire and Release locks
#     - etc.


# with open('test.txt', 'r+') as f:
#     print(f.read())

from contextlib import contextmanager

# Function with context manager functionality

@contextmanager
def open_file(file, mode):
    try:
        f = open(file, mode)
        yield f
    finally:
        f.close()

with open_file('test.txt', 'r') as f:
    print(f.read())

print(f.closed)