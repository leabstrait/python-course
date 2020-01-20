# Get inside a directory, list contents and go back to start directory

import os
from contextlib import contextmanager

# cwd = os.getcwd()
# os.chdir('test_dir_1')
# print(os.listdir())
# os.chdir(cwd)

# cwd = os.getcwd()
# os.chdir('test_dir_2')
# print(os.listdir())
# os.chdir(cwd)


@contextmanager
def change_and_listdir(dest):
    try:
        cwd = os.getcwd()
        os.chdir('test_dir_1')
        yield
    finally:
        os.chdir(cwd)


with change_and_listdir('test_dir_1'):
    print(os.listdir())

with change_and_listdir('test_dir_2'):
    print(os.listdir())
