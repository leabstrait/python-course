num = input("Enter number for primality test: ")

if num == 1:
    print("Not Prime")
for n in range(2, num):
    if num % n == 0:
        print('Not Prime')
        exit()

print("Prime")