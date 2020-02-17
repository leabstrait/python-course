# A test on enclosing scopes
x = 'global'

def outer():
    x = 'outer'
    def inner():
        nonlocal x
        # global x
        x = 'inner'
        print(x)
    inner()
    print(x)

outer()
print(x)