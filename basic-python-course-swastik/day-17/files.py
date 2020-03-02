import random
import os

os.mkdir('randoms')
with open('randoms/test2.txt', 'w') as wf:
    for _ in range(20):
        wf.write(str(random.random()))

# Copying to another file
# with open('texts/test.txt', 'r') as rf:
#     with open('test_copy.txt', 'w') as wf:
#         for line in rf:
#             wf.write(line)

# Copying an image file:
# with open('python.png', 'rb') as source:
#     with open('python_copy.png', 'wb') as dest:
#         for line in source:
#             print(line)
#             dest.write(line)
        

