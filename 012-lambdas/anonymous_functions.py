# A taste of functional programming

# def style
def sum(x, y):
    return x + y

print(sum(3, 7))

# Lambda style
lambda_sum = lambda x, y: x + y

print(lambda_sum(3, 7))


# A recursove fn in lambda notation
factorial = lambda n: 1 if n == 0 else n * factorial(n-1)

print(factorial(5))