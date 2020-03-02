import os

if not os.path.exists('sort_demo'):
    os.mkdir('sort_demo')


# folders= []
# for i in range(0,21):
#     name = f'day-{i}'
#     folders.append(name)


folders = [f'day-{num}' for num in range(0, 21)]
print(sorted(folders))


for folder_name in folders:
    base_path = 'sort_demo'
    our_path = os.path.join(base_path, folder_name)

    if not os.path.exists(our_path):
        os.mkdir(our_path)


folders_2 = [f'day-{str(num).zfill(3)}' for num in range(0, 21)]
print(sorted(folders_2))

# for folder_name in folders:
#     base_path = 'sort_demo'
#     our_path = os.path.join(base_path, folder_name)

#     if not os.path.exists(our_path):
#         os.replace(our_path)

print(os.getcwd())
os.chdir('sort_demo')
print(os.getcwd())
# os.rename(folders, *folders_2)

for i, name in enumerate(folders):
    os.rename(name, folders_2[i])

