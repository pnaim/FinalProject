# Name: Pasha Pradana Naim
# Student ID: 2201814701
# Purpose: Final Project

def help_function():
    print('''Welcome to help center. You need to follow the instructions thoroughly. You can type whatever commands you
    like, but there are some commands which cannot be functioned. Make sure that the command is systematic, like 'Look' 
    or 'Help' and in order to progress, use the directions like 'N' or 'S'. There are no diagonals in this game.''')

def start():
    print('''Welcome to the game, created by Pasha Naim, type start to begin''')
    print()
    prompt_sta()

def prompt_sta():                           #This code is used to begin the game
    prompt_0 = input ("Type a command: ")
    try:
        if prompt_0 == "Start" or "start":
            outside_house()
        elif prompt_0 == "Help" or "help":
            help_function()
            print()
            prompt_sta()
        elif prompt_0 == "Begin":
            print("You need to follow the instructions!")
            print()
            prompt_sta()
        else:
            print("Type start! Not that")
            print()
            prompt_sta()
    except ValueError:
        print("Type start! Not that")
        print()
        prompt_sta()
def outside_house():
    print("""You're now outside a nice-looking house. What are you going to do? Enter, look, exit, or trash flowers""")
    print()
    prompt_outside()
def prompt_outside():                       #This is when we are outside the house
    prompt_1 = input("Type a command: ")
    try:
        if prompt_1 == "Enter" or "enter":
            hallway()
        if prompt_1 == "Help" or "help":
            help_function()
            print()
            prompt_sta()
        if prompt_1 == "Look" or "look":
            print("""You're outside the house. It is very huge. There is a wooden door to the east, and a locked gate to
                  the west. There are a horrid-looking flowers around you waiting to be thrashed.""")
            print()
            prompt_outside()
        if prompt_1 == "Exit" or "exit":
            print("Let's go outside")
            print()
            street()
        if prompt_1 == "Trash flowers" or "trash flowers":
            print("You have trashed the flowers. That's good, man!")
            print()
            prompt_outside()
    except ValueError:
        print("...")
        print()
        prompt_outside()

def hallway():
    print("You're in the hallway. The rooms are in the north and south.")
    print()
    prompt_hallway()
def prompt_hallway():
    prompt_2 = input("Choose your direction, north or south, or exit this house: ")   #This code determines whether we go to the north or south
    try:
        if prompt_2 == 'N' or 'n' or 'North' or 'north':
            lounge()
        elif prompt_2 == 'S' or 's' or 'South' or 'south':
            kitchen()
        elif prompt_2 == "Help" or "help":
            help_function()
            print()
            prompt_hallway()
        elif prompt_2 == "Exit" or "exit":
            street()
        else:
            print("...")
            print()
            prompt_hallway()
    except ValueError:
        print("...")
        print()
        prompt_hallway()

def lounge():
    print("You're in the small lounge, there is an exit to the south")
    print()
    prompt_lounge()
def prompt_lounge():
    prompt_3 = input("Choose your direction: ") #This is when we are in the lounge
    try:
        if prompt_3 == 'S' or 's' or "South" or "south":
            hallway()
        elif prompt_3 == 'N' or 'n' or 'North' or 'north' or 'W' or 'w' or 'West' or 'west' or 'E' or 'e' or 'East' or 'east':
            print("You can't go that way")
            prompt_lounge()
        elif prompt_3 == "Help" or "help":
            help_function()
            print()
            prompt_lounge()
        else:
            print("...")
            print()
            prompt_lounge()
    except ValueError:
        print("...")
        print()
        prompt_lounge()
def kitchen():
    print("You are in the kitchen. There is an exit to the north")
    print()
    prompt_kitchen()
def prompt_kitchen():
    prompt_4 = input("Choose your direction: ")  #This is when we are in the kitchen
    try:
        if prompt_4 == 'N' or 'n' or 'North' or 'north':
            hallway()
        if prompt_4 == 'S' or 's' or 'South' or 'south' or 'W' or 'w' or 'West' or 'west' or 'E' or 'e' or 'East' or 'east':
            print("You cannot go that way")
            prompt_kitchen()
        if prompt_4 == "Help" or "help":
            help_function()
            print()
            prompt_kitchen()
    except ValueError:
        print("...")
        print()
        prompt_kitchen()

def street():
    print("Welcome to the street, you can choose the place that you like")  #We are now proceeding to the street
    prompt_street()
def prompt_street():
    prompt_5 = input("Where are you going?: ")
    try:
        if prompt_5 == "Restaurant" or "restaurant" or "Resto" or "resto":
            print("Let's have some meal")
            street()
            prompt_street()
        if prompt_5 == "Gym" or "gym":
            print("Let's do some workout!")
            gym()
    except ValueError:
        print("...")
        prompt_street()

def gym():
    print("Welcome to the gym, please choose which workout you want")
    prompt_gym()
def prompt_gym():
    prompt_6 = input("What do you want to do?: ")    #This is when we are at the gym
    try:
        if prompt_6 == "Dumb bells" or "dumb bells":
            print("Nice job! You bulked up your biceps and triceps")
            prompt_gym()
        elif prompt_6 == "Treadmill" or "treadmill":
            print("Great! You have burn the fat down from your body")
            prompt_gym()
        elif prompt_6 == "Weight machine" or "weight machine":
            print("You have bulked up your arms, legs, and even your abs. What a great workout")
        else:
            print("...")
            prompt_gym()
    except ValueError:
        print("...")
        prompt_gym()
start()