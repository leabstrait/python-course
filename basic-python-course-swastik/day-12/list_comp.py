# squares = list(map(lambda x: x*x, range(1,11)))

# print(squares)

# squares = []
# for i in range (1,11):
#     squares.append(i**2)

# print(squares)

squares = [x**2 for x in range(1,11) if x % 2 == 0]
print(squares)


print([num for num in range(1,1000) if )
33
330
233
339



alpha = 'abcd' 
num = '1234'

cart_prod = [(a, n) for a, n in zip(alpha, num)]
print(cart_prod)