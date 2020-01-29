remember_calc = {}


def fibo(n):
    if n == 0:
        return 1
    if n == 1:
        return 1        
    else:
        if n-1 not in remember_calc:
            remember_calc[n-1] = fibo(n-1)
        if n-2 not in remember_calc:
            remember_calc[n-2] = fibo(n-2)

        return remember_calc[n-1] + remember_calc[n-2]


print(fibo(2))