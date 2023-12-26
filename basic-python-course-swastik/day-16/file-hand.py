

with open('test.py', 'w') as f:
    print(f.closed)
    for i in range(10):
        f.write('\n# This was added by another program again')

print(f.closed)

del f
