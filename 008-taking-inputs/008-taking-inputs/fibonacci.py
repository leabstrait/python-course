print("Fibonacci Series")
first, second = int(input("Enter a number: ")), int(input("Enter another number: "))
n = int(input("For how many iterations? "))

for i in range(n):
    print(first, sep=" ")
    new = first + second
    first = second
    second = new
    

