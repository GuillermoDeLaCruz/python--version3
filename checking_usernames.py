current_users = ['John', 'gg21',]

new_users = ['JOHN','gg21']

for new_user in new_users:
    if new_user.title() in current_users:
        print("Enter new user name")
    else:
        print("User name is available")
