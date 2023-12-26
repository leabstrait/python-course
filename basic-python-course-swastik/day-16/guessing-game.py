import random 

random_num = random.randint(1, 10)

count = 1

guess = input("Guess a number that I'm holding: ")
while guess != random_num:
    if int(guess) < random_num: print("Too low")
    elif int(guess) > random_num: print("Too high")
    count += 1
    guess = input("Try again: ")
    if guess == 'q': exit()

print(f"Well done! you guessed it! you took {count} tries")