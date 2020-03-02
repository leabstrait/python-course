bikes = ['Pulsar NS 200', 'Honda CBR 600', 'Yamaha R15', 'Honda Shine', 'Yamaha FZ', 'Duke 250', 'Hayabusa 1000', 'Ducati 1000', 'Harley Davidson', 'Royal Enfield']
print('\nTotal bikes we have:', len(bikes), sep=' >>>> ')
print(bikes)

# Access each element from the list
print("\nAccess each element from the list")
print(bikes[0])
print(bikes[1])
print(bikes[2])
print(bikes[3])

# List Slicing
print("\nList Slicing: bikes[5:8]")
print(bikes[5:8])

# Remove the last bike from the list
print("\nRemove the last bike from the list")
last_bike = bikes.pop()
print(last_bike)
print(bikes)

# Append to end of list a new bike
print("\nAppend to end of list a new bike")
bikes.append('Benelli 600i')
print(bikes)

# Edit a bike name at 3rd index
print("\nEdit a bike name at 3rd index")
bikes[3] = "ZX 14R"
print(bikes)

# Insert a bike at position 1
print("\nInsert a bike at position 1")
bikes.insert(1, "Benelli 600i")
print(bikes)

# Delete something from the list at index 4
print("\nDelete something from the list at index 4")
del bikes[4]
print(bikes)

# Remove specific elements 
print("\nRemove specific elements: Pulsar NS 200")
bikes.remove('Pulsar NS 200')
print(bikes)

# Reverse a list
print("\nReverse a list permanently, no sorting")
bikes.reverse()

# Sorting a list and string in a new list
print("\nSorting a list and string in a new list")
bikes_sorted = sorted(bikes)
print('bikes_sorted:', bikes_sorted)


# Sorting a list in place
print("\nSorting a list in place")
print("\nOriginal list")
print(bikes)

print("\nPrint list 'bikes' after sorting in-place")
bikes.sort(reverse = False)
print(bikes)

print("\nPrint list 'bikes' after sorting in-place in reverse order")
bikes.sort(reverse = True)
print(bikes)
