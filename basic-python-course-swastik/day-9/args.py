def sum_all(lon):
    sum = 0
    for num in lon:
        sum = sum + num

    print(sum)

def sum_all_no_list(*nums):
    sum = 0
    for num in nums:
        sum += num

    print(sum)

# sum_all([1, 2, 3, 4, 5, 6, 7, 8, 9])

sum_all_no_list(1, 2, 3, 4, 5, 6, 7, 8,5,6,7,2,6,2,68,7, 9)
