

# Dictionary Comprehensions
alpha = 'abcdefghi'
num = '123456789'

alphanum_dict = {}
for c, i in zip(alpha, num):
    alphanum_dict[c] = i

print(alphanum_dict)

# OR

alphanum_dict = {c: i for c, i in zip(alpha, num)}

print(alphanum_dict)