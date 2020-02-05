the_num = 55
while guess != the_num:
    guess = int(imput("Can you guess the number I'm thinking of? "))
    count = 1
    if guess < compnum:
        print("Too low!")
    else:
        print("Too high!")
    count = count + 1
    guess = int(input(Have another guess: ))

print("Well done! you took", count, "attempts")
