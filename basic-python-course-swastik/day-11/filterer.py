lon = range(1,11)
########################################################
def filterer(fn, lox):
    loff_x = []
    for x in lox:
        if fn(x):
            loff_x.append(x)
    return loff_x

is_odd = lambda n : n % 2 != 0

odd_only = filterer(is_odd, lon)
print(odd_only)

#########################################################
def mapper(fn, lox):
    lofn_x = []
    for x in lox:
        lofn_x.append(fn(x))
    return lofn_x

square = lambda x: x*x

squares = mapper(square, lon)
print(squares)

