prompt = "\nPlease enter the name of the city you visted:"
prompt += "\nEnter 'quit' to end the program "


while True:
    city = input(prompt)

    if city == 'quit':
        break
    else:
        print("I'd love to go to " + city.title() + "!")














