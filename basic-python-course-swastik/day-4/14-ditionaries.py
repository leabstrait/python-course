python_class = {
    36: 'sanjay',
    1: 'karma',
    7: 'badri',
    5: 'arun'
}

python_people = {
    'sanjay': 'dhakal',
    'karma' : 'ghising',
    'badri' : 'aran',
    'arun'  : 'khanal'
}

print(python_class[1])
print(python_people['arun'])


print(python_class)
print(python_class.keys())
print(sorted(python_class.keys()))


for roll_num in sorted(python_class.keys()):
    print(f'Roll NUmber {roll_num} is {python_class[roll_num]}')








# print(type(python_class))

for person, desc in python_class.items():
    print(person, 'is a', desc)

# for key, value in python_class.items():
#     print(key, value)

for x in python_class.keys():
    print(x)

for y in python_class.values():
    print(y)
