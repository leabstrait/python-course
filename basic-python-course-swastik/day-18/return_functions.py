sansa = int

def decorate(func):
    def make_stars(*args):
        print('*'*20)
        func(*args)
        print('*'*20)
    return make_stars

@decorate
def add(x, y):
    print(x + y)

add(1,2)

@decorate
def tyrion(fullname):
    name_length = len(fullname)
    print(fullname[:sansa(name_length/2)])

tyrion("Sansa Stark")

@decorate
def print_name(fullname):
    print(fullname)

print_name("Sanjay Dhakal")


# make_stars(print_name, 'Aditya Joshi')
# make_stars(tyrion, 'Pushpa Neupane')
# make_stars(add, 1, 2)

# add_starred = decorate(add)
# tyrion_starred = decorate(tyrion)
# name_starred = decorate(print_name)

# add_starred(1,2)
# tyrion_starred("Badri Raj Aran")
# name_starred("Arun Khanal")