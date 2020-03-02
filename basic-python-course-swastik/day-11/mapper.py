def mapper(fn, lox):
    lofn_x = []
    for x in lox:
        lofn_x.append(fn(x))
    return lofn_x

lon = range(1,11)

square = lambda x: x*x

losq = mapper(square, lon)
print(list(lon))
print(losq)