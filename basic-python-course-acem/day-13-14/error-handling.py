# try:
#     pass
# except expression as identifier:
#     pass
# else:
#     pass
# finally:
#     pass

try:
    # new_var = non_existent_var
    # d = 1/0
    # nums = [1,2,3]
    # print(nums[5])
    nu = 0
    de = 0
    if de == 0 and nu == 0:
        raise BaseException("Zero numerator and  denominator")
    else:
        q = nu / de
        print(q)
except ZeroDivisionError as ze:
    # print("divsion by zero occured")
    print(ze)
except NameError as ne:
    print(ne)
except Exception as e:
    print("yes")
    print(e)
else:
    print("there are no errors")
finally:
    print("This executes no matter what")

print("This is a useful statement to print")