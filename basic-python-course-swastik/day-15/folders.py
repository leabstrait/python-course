import os 

def create_subfolders(basedir, ndays):
    if not os.path.exists(basedir):
        os.mkdir(basedir)
    os.chdir(basedir)
    for i in range(1,ndays+1):
        dirname = 'day-'+str(i)
        if not os.path.exists(dirname):
            os.mkdir(dirname)
    print(os.getcwd(), 'has been created')
    os.chdir('../')


create_subfolders('testzone', 20)
create_subfolders('testzone2', 10)

