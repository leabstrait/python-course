lon = [num ** 2 for num in range(1, 11)]

print(lon)
# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# WAPP find if 36 is in the list and at which index 
our_num = 36

# idx = 0
# for num in lon:
#     if num == our_num:
#         found = 'yes'
#         break    
#     idx = idx + 1

# print(found, 'at index:', idx)

is_in_list = our_num in lon
if is_in_list == True:
    print('yes at index: ', lon.index(our_num))

