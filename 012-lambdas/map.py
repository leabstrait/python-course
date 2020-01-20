def fahrenheit(T):
    return ((float(9)/5)*T + 32)

def celsius(T):
    return (float(5)/9)*(T-32)

temperatures_in_abs = (36.5, 37, 37.5, 38, 39)
print(temperatures_in_abs)

temperatures_in_fahr = map(fahrenheit, temperatures_in_abs)
print(temperatures_in_fahr)

temperatures_in_cel = map(celsius, temperatures_in_fahr)
print(temperatures_in_cel)


# Using Lambdas
# ....


# Map with multiple lists
a = [1, 2, 3, 4]
b = [17, 12, 11, 10]
c = [-1, -4, 5, 9]

print(list(map(lambda x, y : x+y, a, b)))

print(list(map(lambda x, y, z : x+y+z, a, b, c)))

print(list(map(lambda x, y, z : 2.5*x + 2*y - z, a, b, c)))


# Map a list of functions

from math import sin, cos, tan, pi

trigs = [sin, cos, tan]

trig_vals = lambda num: list(map(lambda fn: fn(num), trigs))

print(trig_vals(pi/2))