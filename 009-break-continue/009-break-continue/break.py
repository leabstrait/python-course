import time
nonsense = 'This is a gibberish statement. Oh, When will it stop? I think a semicolon will do the trick. I will just end this now; Hey did it stop'

for char in nonsense:
    if char == ';':
        break
    else:
        time.sleep(0.5)
        print(char)