# Find if a number is in a list and if yes, at which position
the_list = [12, 346, 236, -235, 854, 2345, 835]
our_num = 2345

idx = 0
for num in the_list:
    if num == our_num:
        found = 'yes'
        break
    idx = idx + 1

print(found, 'at index: ', idx)


# Shorthand 
is_in_list = our_num in the_list
if is_in_list:
    print('yes at index: ', the_list.index(our_num))