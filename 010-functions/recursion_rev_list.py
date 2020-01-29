def rev_list(lon):
    
    if len(lon) == 0:
        return []
    else:
        return rev_list(lon[1:]) + [lon[0]]


print(rev_list([1,2,3,4,5]))