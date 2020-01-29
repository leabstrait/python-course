import csv

with open('Attendance_tabs.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    # csv_reader = csv.reader(csv_file, delimiter='\t')       # Need to use \t as delimiters
    
    for line in csv_reader:
        print(line)
