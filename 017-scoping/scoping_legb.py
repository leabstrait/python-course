"""
LEGB
Local, Enclosing, Global, Built-in
"""

# Local - Global
# -------------------------------------------

g = 'global g'


def test(l_fn):
    global g        # makes g global, modifies global g
    l = 'local l'
    g = 'local g'   # Local g variable
    print(g)
    print(l)
    print(l_fn)

print(g)
# print(l)      # Doesn't work
test('local l_fn')
# print(l_fn)      # Doesn't work

# Built-in
# -------------------------------------------
print(min([1,2,34,6,0]))

def min(num_list):
    return max(num_list)

print(min([1,2,34,6,0]))

# Enclosing
# -------------------------------------------
x = 'non enclosed x'
def outer():
    x = 'outer x'

    def inner():
        # global x          # we could do this to let x away from this enclosing scope but it'll overwrite the global scope but not the enclosing one.
        # nonlocal x        # instead we do this 
        x = 'inner x'       # try removing this line
        print(x)

    inner()
    print(x)

outer()
print(x)