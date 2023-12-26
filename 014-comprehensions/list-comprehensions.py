
squares_lstmap = map(lambda value: value**2, range(1, 11))

evennums_filter = filter(lambda value: value % 2 == 0, range(1, 11))

alphanum_zip = zip('abcd', '1234')

squares_lstcomp = [value**2 for value in range(1, 11)]

evennums_lstcomp = [value for value in range(1, 11) if value % 2 == 0]

alphanum_lstcomp = [(c, i) for c in 'abcd' for i in '1234']


print(list(squares_lstmap))
print(list(evennums_filter))

print(squares_lstcomp)
print(evennums_lstcomp)

print(alphanum_lstcomp)

print(list(alphanum_zip))
