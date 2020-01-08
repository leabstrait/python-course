bikes = ['Pulsar NS 200', 'Honda CBR 600', 'Yamaha R15', 'Honda Shine', 'Yamaha FZ', 'Duke 250', 'Hayabusa 1000', 'Ducati 1000', 'Harley Davidson', 'Royal Enfield']
print('Total bikes we have:', len(bikes), sep=' ------>>>> ')
print(bikes)

# Access each element from the list
print()

print(bikes[0])
print(bikes[1])
print(bikes[2])
print(bikes[3])


# List Slicing
print()

print(bikes[5:8])


# Remove the last bike from the list
print()

last_bike = bikes.pop()
print(last_bike)
print(bikes)

# Append to end of list a new bike
print()

bikes.append('Benelli 600i')
print(bikes)

# Edit a bike name at 3rd index
print()

bikes[3] = "ZX 14R"
print(bikes)

# Insert a bike at position 1
print()

bikes.insert(1, "Benelli 600i")
print(bikes)

# Delete something from the list at some index
print()

del bikes[4]
print(bikes)

# Remove specific elements 
print()

bikes.remove('Pulsar NS 200')
print(bikes)


# Sorting a list and string in a new list
print("\nSorting a list and string in a new list")
bikes_sorted = sorted(bikes)
print(bikes_sorted)


# Sorting a list in place
print()
print(bikes)
print()

bikes.sort(reverse = False)
print(bikes)
print()

bikes.sort(reverse = True)
print(bikes)

# Reverse a list
print()
bikes.reverse()

