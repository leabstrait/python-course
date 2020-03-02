import os
import datetime as dt

def mero_class_ko_notes(base_dir, days):
    """
    Takes in the Course name and duration in days\n
    makes a folder structure for the class notes, \n
    with a predefined template 
    """

    try:
        os.mkdir(base_dir)
    except FileExistsError as fe:
        print(fe)
    else:
        for i in range(1, days + 1):
            day_dir = base_dir + "/Day " + str(i)
            if not os.path.exists(day_dir):
                os.mkdir(day_dir)
                
            
            with open(f"{day_dir}/Day {i} Notes", 'w') as day_file:
                daily_date = dt.datetime.now() + dt.timedelta(days=i)
                daily_date = daily_date.strftime("%B/%d/%Y")
                day_file.write(f"Date: {daily_date}")


# base_dir = 'Python Class'
# days = 30
mero_class_ko_notes("Rust Class", 40)
mero_class_ko_notes("javascript Class", 30)