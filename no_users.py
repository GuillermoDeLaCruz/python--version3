#usernames = ['apple_27', 'guyonwheels21', 'admin', 'jellybean', 'bananas_23']
usernames = []

if len(usernames) != 0:
    for username in usernames:
        if username == 'admin':
            print("Hello admin, would you like to see a staus report?")
        else:
         print("Hello " + username + ", thank you for loging in again.")
else:
    print("We need to find some users!")