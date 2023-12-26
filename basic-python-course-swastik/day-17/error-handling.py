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
    # impossible = 1/0
    nums = [1,2,3]
    print(nums[5])
except NameError as ne:
    print('An error occured 1')
    print(ne)
except ZeroDivisionError as ze:
    print('An error occured 2')
    print(ze)
except IndexError as ie:
    print('An error occured 3')
    print(ie)
except Exception as e:
    print('An error occured 4')
    print(e)
else:
    print("There is/are no error(s)")
finally:
    print("This executes no matter what")

print("this is a useful statement to print")
