def mapper(fn_x, lox):
    lofn_x = []
    for x in lox:
        lofn_x.append(fn_x(x))
    return lofn_x

square = lambda num : num** 2

lon = [1,2,3,4,5,6]

losq = mapper(square, lon)

# print(lon)
# print(losq)


c_to_f = lambda c : 1.8*c + 32

lot_c = [20, 25, 21.4, 36, 39, 40]

lot_f = mapper(c_to_f, lot_c)

lot_f_builtin = map(c_to_f, lot_c)

# print(lot_c)
# print(lot_f)

# print(list(lot_f_builtin))

a = [1, 2, 3]
b = [3, 2, 1]
c = [1, 1, 1]

print(list(map(lambda x, y, z: x+y+z, a, b, c)))