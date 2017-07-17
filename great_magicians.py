names = ['aaa', 'bbbb', 'cccc', 'dddd', 'eeeeeee']
great = []

def show_magicians(list):
    """

    """
    while list:
        current_item = list.pop()
        print(current_item)


def make_great(list, great):

    while list:
        current_item = "Great " + list.pop()
        
        great.append(current_item)





make_great(names[:], great)
show_magicians(great[:])


