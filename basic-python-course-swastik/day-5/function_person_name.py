def person_info(fname, lname, age, mname='bdr'):
    new_fname = fname.title().strip()
    new_mname = mname.title().strip()
    new_lname = lname.title().strip()

    output = f"{new_fname} {new_mname} {new_lname} is {age} years old"

    return output

first_name = input("Your first name: ")
middle_name = input("Your middle name: ")
last_name = input("Your last name: ")
age = input("Your age: ")

output_name = person_info(first_name, last_name, age, middle_name)

output_name_2 = person_info(first_name, last_name, age)

print(output_name)
# print(output_name_2)


