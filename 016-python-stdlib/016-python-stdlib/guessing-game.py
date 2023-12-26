import random

the_num = random.randint(1, 100)
count = 0
guess = int(input("Can you guess the number I'm thinking of? "))
while guess != the_num:
    print("Too low!" if guess < the_num else "Too high!")
    count = count + 1
    guess = int(input("Have another guess: "))

print("Well done! you took", count, "attempts")
