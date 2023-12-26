string = "This is Python 3.8.1"

alphas= nums= spaces= others = 0
for ch in string:
    if ch.isalpha():
        alphas += 1
    elif ch.isnumeric():
        nums += 1
    elif ch.isspace():
        spaces += 1
    else:
        others += 1

print(f"Alphabets: {alphas}\nDigits: {nums}\nSpaces: {spaces}\nOthers: {others}")