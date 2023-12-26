import os
import datetime as dt

course_dir = "Python Course"

try:
    os.mkdir(course_dir)
except FileExistsError:
    print("The folder already exists, So this program will exit to avoid overwriting")
    
else:
    day_dirs = [f"Day-{i}" for i in range(1, 21)]
    os.chdir(course_dir)
    for day_dir in day_dirs:
        try:
            os.mkdir(day_dir)
        except Exception:
            print("The day's folder already exists")
        else:
            print(day_dir, "was created")
        

    for i in range(20):
        day_file = open(f"{day_dirs[i]}/Notes.note", 'w')
        today= dt.datetime.now() + dt.timedelta(days=i)
        today = f"{today.year}-{today.month}-{today.day}"
        day_file.write(str(today))
    
    os.chdir('..')

finally:
    day_file.close()

print(day_file.closed)

