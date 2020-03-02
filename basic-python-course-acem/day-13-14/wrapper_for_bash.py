import subprocess
import os


# help(subprocess)


out = subprocess.run('python -m uppperizer.py')
print(os.getcwd())

print(type(out))