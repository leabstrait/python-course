# list comprehensions exercises

q1 = "Count the number of spaces in a string, this string"
spaces = [char for char in q1 if char == ' ']
len(spaces)

q2 = "Remove all of the vowels in a string, i.e make of list of \
    characters other than the vowels"
vowels = 'aeiou ,.'
cons = [char for char in q2 if char not in vowels]
cons

cons = filter(lambda c: c not in vowels, q2)
list(cons)

q3 = "Find all of the words in a string that are less than 4 letters" 
[word for word in q3.split() if len(word) < 4]

filter()
