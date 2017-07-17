age = 0


if age < 2:
    person = 'baby'
elif age >= 2 and age < 4:
    person = "toddler"
elif age >= 4 and age < 13:
    person = "kid"
elif age >= 13 and age < 20:
    person = "teenager"
elif age >= 20 and age < 65:
    person = "adult"
else:
    person = "elder"
print("Person is a " + person)