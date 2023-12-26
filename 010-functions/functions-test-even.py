def is_even_text_version(num):
    if num % 2 == 0:
        print('Even')
    else:
        print('Odd')

def is_even_return_version(num)
    if num %2 == 0:
        return 'Even'
    else:
        return 'Odd'

num = 4

is_even_text_version(num)
print(is_even_text_version(num))


# A shorter style


# def even_or_not(num):
#     return 'yes' if num % 2 == 0 else 'no'

# print(even_or_not(3))


even_or_not_lambda = lambda num: 'yes' if num % 2 == 0 else 'no'

print(type(even_or_not_lambda))