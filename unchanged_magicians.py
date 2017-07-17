names = ['aaa', 'bbbb', 'cccc', 'dddd', 'eeeeeee']
great = []


def show_magicians(lists):
    """

    """
    for list in lists:
        print(list)


def make_great(list, great):
    while list:
        current_item = "Great " + list.pop()

        great.append(current_item)


make_great(names[:], great)
show_magicians(great[:])

print(names)
print(great)

