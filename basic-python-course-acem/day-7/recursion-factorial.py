def fact(n):
    acc = 1
    for i in range(1, n+1):
        acc *= i

    return acc


def fact2(n):
    acc = 1
    for i in range(n, 0, -1):
        acc *= i

    return acc
    

def fact_rec(n):
    if n == 1 :
        return n

    else:
        return n * fact_rec(n - 1)



print(fact(6))
print(fact2(6))
print(fact_rec(6))