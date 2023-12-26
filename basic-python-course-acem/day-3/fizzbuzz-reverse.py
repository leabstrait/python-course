lon = range(1, 40)

lofb = []

for n in lon:
    if n % 3 == 0 and n % 5 == 0:
        lofb.append('fizzbuzz')
    elif n % 3 == 0:
        lofb.append('fizz')
    elif n % 5 == 0:
        lofb.append('buzz')
    else:
        lofb.append(n)

print(lofb)


ctr = 0
for item in lofb:
    if item == 'fizz' or item == 'buzz' or item == 'fizzbuzz':
        lofb[ctr] = ctr + 1
    ctr += 1


print(lofb)


