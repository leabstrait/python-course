import csv

with open('Attendance.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)

    with open('Attendance_tabs.csv', 'w') as new_file:
        # csv_writer = csv.writer(new_file, delimiter='-')    # In new file change delimiter to '-'
        csv_writer = csv.writer(new_file, delimiter='\t')    # In new file change delimiter to '\t'

        for line in csv_reader:
            csv_writer.writerow(line)
