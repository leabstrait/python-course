# File objects

f = open('test.txt', 'r+')

print(f.name)
print(f.mode)
print(f.read())

print(f.closed)
f.close()
print(f.closed)


# Using Context Managers

with open('test.txt', 'r+') as f:
    print(type(f))
    print(f.name)
    print(f.mode)
    print(f.read())      
    print(f.readlines())
    print(f.readline())

print(f.closed)


# Copying a file
with open('test.txt', 'r') as rf:
    with open('test_copy.txt', 'w') as wf:
        for line in rf:
            wf.write(line)

# Copying a file binary
with open('python.png', 'rb') as rf:
    with open('python_copy.png', 'wb') as wf:
        for line in rf:
            wf.write(line)


# Optional - with chunking
with open('python.png', 'rb') as rf:
    with open('python_copy.png', 'wb') as wf:
        chunk_size = 4096
        rf_chunk = rf.read(chunk_size) 
        while len(rf_chunk) > 0:
            wf.write(rf_chunk)
            rf_chunk = rf.read(chunk_size) 