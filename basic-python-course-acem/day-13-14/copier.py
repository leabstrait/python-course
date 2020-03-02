

with open('file.txt', 'r') as rf:
    with open('file_copy.txt', 'w') as wf:
        rc = rf.read()
        wf.write(rc)

with open('python.png', 'rb') as rf:
    with open('python_copy.png', 'wb') as wf:
        rc = rf.read()
        wf.write(rc)
