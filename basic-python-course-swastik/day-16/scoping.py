
x = 'global'

def outer():
    x = 'outer'
    def inner():
        y = 'inner'
        # print(x)
        nonlocal x
        x = 'changed outer'
        print(x)
        print(y)

    print(x)
    inner()
    print(x)

print(x)
outer()
print(x)