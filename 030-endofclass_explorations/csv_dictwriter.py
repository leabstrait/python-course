import csv

with open('Attendance.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file, delimiter=',')
    

    with open('Attendance_dict', 'w') as new_file:
        fieldnames = ['name', 'day01', 'day02', 'day03', 'day04', 'day05', 'day06', 'day07', 'day08', 'day09', 'day10', 'day11', 'day12', 'day13', 'day14', 'day15', 'day16', 'day17', 'day18', 'day19', 'day20', 'day21', 'day22', 'day23']
    
        csv_writer = csv.DictWriter(new_file, fieldnames=fieldnames, delimiter='\t')

        csv_writer.writeheader()

        for line in csv_reader:
            csv_writer.writerow(line)
