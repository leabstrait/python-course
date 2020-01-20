
# f = open('test.tst')        # Gives error due to typo

try:
    f = open('test.txt')
    # var = non_existent_var     # This has error but we print out file not found
    if f.name == 'test.txt':
        raise Exception("FileName error")
# except FileNotFoundError:
#     print("Sorry, This file doesn't exist")
except Exception as e:
    # Specific exceptions at top, general most below
    print(e)
else:
    print(f.read())
    f.close()
finally:
    print("Operation Finished!")
