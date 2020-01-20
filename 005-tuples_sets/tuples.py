# Tuples 
coordinates = ('27.2038° N', '77.5011° E')

lattitude = coordinates[0]
longitude = coordinates[1]

print(lattitude)
print(longitude)

# coordinates[0] = 'random stuff'    # Tuples are immutable

for value in coordinates:
    print(value)
