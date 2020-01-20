import os

# Finding help

# print(dir(os))
# print(help(os))

print(os.getcwd())

os.chdir('/home/labin')

print(os.getcwd())

print(os.listdir())

os.mkdir('single_dir')

os.makedirs('main_dir/sub_dir')

os.rmdir()

os.removedirs()

os.rename(src, dst)

os.stat(path)

os.walk(origin)

os.environ.get('HOME')

print(dir(os.path))