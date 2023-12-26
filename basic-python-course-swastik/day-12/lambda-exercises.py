fullname = lambda fname, lname: f"{fname.title()} {lname.title()}"
print(fullname('labin', 'ojha'))

[1,2,3,4,5,6,7,8,13,745,123,82,3,852,2]

swap = lambda x, y: (y, x)
x = 'first'
y = 'second'
x, y = swap(x, y)
print(x, y)

a = [1,2,3,4,5,6]
b = [1,3,7,5]

print(list(filter(lambda x: x in b, a)))

students = {'arun': 5,
            'sanjeeb': 6,
            'sanjay': 1,
            'sagar': 28,
            'neha': 16,
            'rajan': 20
            }

sorted(students)
sorted(students, key=lambda name: students[name])
