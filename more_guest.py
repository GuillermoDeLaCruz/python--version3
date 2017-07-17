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
guest_list.insert(2, 'Nice')
guest_list.append('jen')

print("Hello, " + guest_list[0])
print("Hello, " + guest_list[1])
print("Hello, " + guest_list[2])
print("Hello, " + guest_list[3])
print("Hello, " + guest_list[4])
print("Hello, " + guest_list[5])

