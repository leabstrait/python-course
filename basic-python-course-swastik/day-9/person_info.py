def person(fname, lname, age, mname=""):

    return f"My name is {fname} {mname} {lname}, and my age is {age}"


full_name = person("Badri","Aran", 20, "Raj")
full_name_2 = person("Sanjay","Dhakal", 22)

print(full_name)
print(full_name_2)