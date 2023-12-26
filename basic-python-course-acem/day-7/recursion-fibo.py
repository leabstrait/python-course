import time


def fibo(n):
    if n == 0:
        return 1
    if n == 1:
        return 1        
    else:
        return fibo(n-1) + fibo(n-2)


start = time.time()

print(fibo(15))

end = time.time()

print("time taken: ", end-start)

start = time.time()

print(fibo(25))

end = time.time()

print("time taken: ", end-start)

start = time.time()

print(fibo(35))

end = time.time()

print("time taken: ", end-start)

start = time.time()

print(fibo(36))

end = time.time()

print("time taken: ", end-start)