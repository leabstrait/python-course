import csv

with open('Attendance.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)

    # To skip the header row
    next(csv_reader)

    for line in csv_reader:
        # Print each line
        print(line) 

        # Print each line at index 0
        # i.e just the names
        print(line[0])