# Context Managers:
# Use Cases:
#     - Close off files after use
#     - Close connection to databases automatically
#     - Acquire and Release locks
#     - etc.


# with open('test.txt', 'r+') as f:
#     print(f.read())

# Class with context manager functionality

class Open_File():
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file
    
    def __exit__(self, exc_type, exc_val, traceback):
        self.file.close()

with Open_File('test.txt', 'r') as f:
    print(f.read())

print(f.closed)