set_1 = set([1, 1, 1, 2, 3, 4, 4, 6, 5])
print(set_1)

set_2 = {1, 3, 5, 6, 7, 9, 11, 13, 3}
print(set_2)

set_3 = set()
set_3.add(2)
set_3.add(0)
set_3.add(4)
set_3.update([6, 8, 10, 12])
print(set_3)

set_1.update(set_1, set_3, [20, 21, 22])
print(set_1)

set_1.remove(0)
print(set_1)

set_4 = set_1.intersection(set_2)
print(set_4)

set_5 = set_2.union(set_3)
print(set_5)


# Sets are performant for membership tests
# if x in list/set:

# O(n) for list
# O(1) for set