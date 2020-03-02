

def starrer(func):
    def caller(*args):
        print('*'*10)
        print(func(*args))
        print('*'*10)

    return caller

@starrer
def add(x,y):
    return x + y

# starry_add = starrer(add)

add(1,2)
