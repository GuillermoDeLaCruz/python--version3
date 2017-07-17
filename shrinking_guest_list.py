# 3-5 changing Guest List
guest_list = ['Memo', 'mom', 'dad']
print(guest_list)

print("Hello, " + guest_list[0])
print("Hello, " + guest_list[1])
print("Hello, " + guest_list[2])

print("Memo, mom, and dad can't make on the day!")

guest_list[0] = 'Guillermo'
guest_list[1] = 'Less'
guest_list[2] = 'Ou'

print("Hello, " + guest_list[0])
print("Hello, " + guest_list[1])
print("Hello, " + guest_list[2])

print("Found three more people to invite")

guest_list.insert(0, 'stephanie')
guest_list.insert(1, 'Nice')
guest_list.append('jen')

print("Hello, " + guest_list[0])
print("Hello, " + guest_list[1])
print("Hello, " + guest_list[2])
print("Hello, " + guest_list[3])
print("Hello, " + guest_list[4])
print("Hello, " + guest_list[5])


print("Change in plans, I can only invite two people")


name = guest_list.pop()
print("Sorry you couldn't make it " + name)

name = guest_list.pop()
print("Sorry you couldn't make it " + name)

name = guest_list.pop()
print("Sorry you couldn't make it " + name)

name = guest_list.pop()
print("Sorry you couldn't make it " + name)

print(guest_list[0] + ', ' + guest_list[1] + " You're still invited ")

del guest_list[0]
#del guest_list[1]
print(guest_list)
