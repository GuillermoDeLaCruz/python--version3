motorcycles = ['handa', 'yamaha', 'suzuki']
print(motorcycles)
motorcycles[0] = 'ducati'
print(motorcycles)

motorcycles.append('ducati')
print(motorcycles)

motorcycles.insert(0, 'ducati')
print(motorcycles)

del motorcycles[0]
print(motorcycles)

del motorcycles[1]
print(motorcycles)

popped_motorcycles = motorcycles.pop()
print(motorcycles)
print(popped_motorcycles)

last_owned = motorcycles.pop()
print("The last motorcycle I owned was a " + last_owned.title() + ".")

first_owned = motorcycles.pop(0)
print('The first motorcycle I owned was a ' + first_owned.title() + '.')

motorcycles_list_two = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles_list_two)

#motorcycles_list_two.remove('ducati')
#print(motorcycles_list_two)

too_expensive = 'ducati'
motorcycles_list_two.remove(too_expensive)
print(motorcycles_list_two)
print("\nA " + too_expensive.title() + " is too expensive for me.")












