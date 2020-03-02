

# def capitalizer(func):
#     return func().upper()

def capitalizer(func):

    def wrapper():
        print(func().upper())

    return wrapper

@capitalizer
def take_name():
    name = input("Enter your name: ")
    return name


take_name()
# capitalled = capitalizer(take_name)

# capitalled()()