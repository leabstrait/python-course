
greet = "Hello"
# name = "Sanjeeb"
name = input("Your Name: ")
name_sanitized = name.strip()

greeting = f"{greet}, {name_sanitized}!"

greeting2 = "{}, {}!".format(greet, name_sanitized)

print(greeting)
print(greeting2)