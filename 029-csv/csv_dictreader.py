import csv

with open('Attendance.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file, delimiter=',')
    
    for line in csv_reader:
        # print(line)
        print(line[' day01'], line[' day06'], sep='\t')
