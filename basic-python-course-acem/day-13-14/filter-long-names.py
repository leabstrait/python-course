with open('name.txt', 'r') as names_file:
    with open('name5.txt', 'w') as names5_file:
        names = names_file.readlines()

        for name in names:
            name = name[:-1]
            try:
                if len(name) > 5:
                    raise Exception(f"Name length of {name} is greater than 5")
                else:
                    names5_file.write(name + '\n')

            except Exception as e:
                print(e)

            else:
                print(f"Wrote {name} to new file")


