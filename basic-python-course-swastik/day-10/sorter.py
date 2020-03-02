def sort_this(los):
    return sorted(los)

def sort_these_names(*names):
    return sorted(names)

def sort_these_keyed_names(**knames):
    # print(knames)
    # print(type(knames))
    # print()
    # print(knames.keys())
    # print(knames.values())

    return sorted(knames.values())

my_students = ['sabin', 'khusbu', 'deependra', 'badri', 'karma']

# print(sort_this(my_students))

# print(sort_these_names('sabin', 'khusbu', 'deependra', 'badri', 'karma'))

print(sort_these_keyed_names(name1='sabin', name2='khusbu', name3='deependra', name4='badri', name5='karma'))