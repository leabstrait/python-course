num = 0

while num <= 20:
    if num % 2 == 0:
        num += 1
        continue
    else:
        print(num)
        num += 1