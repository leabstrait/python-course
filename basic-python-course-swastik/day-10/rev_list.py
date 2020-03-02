def list_rev(lox):
    if len(lox) == 1:
        return [lox[0]]
    else:
        return list_rev(lox[1:]) + [lox[0]]









print(list_rev([1, 2, 3, 'a', 'g']) == ['g', 'a', 3, 2, 1])

print(list_rev([1, 2, 3, 'a', 'g']))
