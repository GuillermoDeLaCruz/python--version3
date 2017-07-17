def greet_user(first_name, last_name):
    """Return a full name, neatly formatted."""
    first_name = first_name + ' ' + last_name
    return first_name.title()


# This is a infinite loop!
"""
while True:
    print("\nPlease tell me your name:")
    f_name = input("Fist name: ")
    l_last = input("Last name: ")

    formatted_name = greet_user(f_name,l_last)
    print("\nHello, " + formatted_name + "!")

"""
while True:
    print("\nPlease tell me your name:")
    print("(enter 'q' at any time to quit)")

    f_name = input("Fist name: ")
    if f_name == 'q':
        break

    l_last = input("Last name: ")
    if l_last == 'q':
        break

    formatted_name = greet_user(f_name,l_last)
    print("\nHello, " + formatted_name + "!")











