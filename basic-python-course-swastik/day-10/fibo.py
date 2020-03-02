# Fibonacci 1 1 2 3 5 8 13 21 .... 
remember_calc = {}

def fibo(n):
    if n == 0 or n == 1:
        return 1
    else:
        if n-1 not in remember_calc:
            remember_calc[n-1] = fibo(n-1)
        if n-2 not in remember_calc:
            remember_calc[n-2] = fibo(n-2)

        return remember_calc[n-1] + remember_calc[n-2]
    

for i in range(40000):
    print(fibo(i))


