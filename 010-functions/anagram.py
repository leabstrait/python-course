def is_anagram(w1, w2):
    if len(w1) == len(w2):
        for c in w1:
            if c in w2:
                still_true = True
            else:
                still_true = False

        return still_true
    return False


def is_anagram_2(w1, w2):
    if len(w1) == len(w2):
       return set(w1) == set(w2)
    return False

def is_anagram_3(w1, w2):
    return sorted(list(w1))== sorted(list(set(w2)))


def is_anagram_4(w1, w2):
    charcount_1 = {}
    charcount_2 = {}

    for char in w1:
        if char not in charcount_1:
            charcount_1[char] = 0
        charcount_1[char] += 1

    for char in w2:
        if char not in charcount_2:
            charcount_2[char] = 0
        charcount_2[char] += 1

    return charcount_1 == charcount_2


print(is_anagram('mango', 'ongma'))

# Corner case, revise code
print(is_anagram('mann', 'namm'))
print(is_anagram_2('nmago', 'omgna'))
print(is_anagram_3('mango', 'goman'))  

print(is_anagram('happy', 'pyha'))
print(is_anagram_2('happy', 'pyha'))
print(is_anagram_3('happy', 'pyha'))



