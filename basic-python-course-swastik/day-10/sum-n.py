def sum_n(n):
    if n == 0:
        return 0
    else:
        return n + sum_n(n-1)

def sum_l(lon):
    if len(lon) == 1:
        return lon[0]
    else:
        return lon[0] + sum_l(lon[1:])

print(sum_n(10) == 55)
print(sum_n(100))

print(sum_l([1,2,3,4,5,6,7,8,9,10]))