def PersonInfo(first_name=input(), last_name=input(), age=input(), middle_name=input()):
    """ Takes first name, last name and returns full name \n 
    Input: first_name, last_name \n
    Output: Fullname

    """
    if len(middle_name) != 0:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = first_name + " " + last_name

    age = "age is " + " " + str(age)

    return {'full name': full_name,
            'age'      : age 
            }


person_info = PersonInfo()

print(person_info)