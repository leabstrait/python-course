current_users = ['badri', 'sanjay', 'arun', 'rajan', 'sabin']
new_users = ['labin', 'sanjay', 'sabin']

# if any new user is in current user list print out already exists
# else print our succesfully registered

for new_user in new_users:
    if new_user in current_users:
        print(f'{new_user} already exists')
    else:
        print(f'{new_user} registered')
        current_users.append(new_user)
        new_users.remove(new_user)

print(current_users)
# ['badri', 'sanjay', 'arun', 'rajan', 'sabin', 'labin']
print(new_users)
# [ 'sanjay', 'sabin']

