def sum_list(lon):
    if len(lon) == 1:
        return lon[0]
    else:
        lon[1] = lon[0] + lon[1]
        return sum_list(lon[1:])


    

print(sum_list([1,2,3,4,5,6,7,8,9,10]))