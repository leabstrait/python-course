# lambda params: do something with params, automatically returns

sum_l = lambda x, y: x + y

print(sum_l(1,2))


sum_l_args = lambda *args: sum(args)

print(sum_l_args(1,2,3))



factorial = lambda n: 1 if n == 1 else n * factorial(n-1)
print(factorial(6))