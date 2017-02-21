#ex36v2.py Version changes, added get_choices function and changed the way text was generated


#Variables
points = 0
border = '=' * 80

intro = """

%s

Welcome to the land of Ammusia. May your choices guide you along your path.
Best of luck adventurer.

%s

You find yourself surrounded in an unknown setting.
In front of you is a pedastal containing two bright buttons.
One red.
One green.
Which button do you press?

""" % (border, border)


math_text = """
%s
You have entered the archway to find yourself in another dimly lit room.
A monitor drops from the ceiling in front of you.

It turns on and and you see an image of a jester pointing at you.

"Welcome to the hall of math puzzles. Pick a difficulty and score some points.", he says.
"Get my questions right and you'll be one step closer to the prize."
"Get them wrong, and pay the ultimate price. Mweheahahahahaha. *cough*"

"Now, what type of question would you like to answer?

1. Arithmetic
2. Funcitons
3. Calculus
4. Go back to the main archway.
5. Push the red button.

"""

green_text = """
%s
Suddenly you find yourself transported into a room dimly light by torch light.
In your pocket you realize there's a small trinket with a pulsing red button.
You look up and realize there are 3 archways before you.
One says Math
Another says Science
Another says ?????

What will you do?

1. Go down through the math hallway
2. Go through the science hallway
3. Go through the mystery hallway
4. Push the button on the trinket

"""

#Funcitons

def start():
    print intro
    red_green()

def red_green():
    print "1. The red button."
    print "2. The green button."
    choice = raw_input("\n> ")
    if choice == "1" or choice == 'red':
        red()
    elif choice == "2" or choice == 'green':
        green()
    else:
        print "That's not a valid choice."
        red_green()

def arch_room(arch):
    arch = eval(arch)
    arch()

def math():
    print math_text % border
    categories = ['arithmetic', 'functions', 'calculus','green', 'red']
    get_choices(categories,math)

def arithmetic():
    print "arithmetic"

def functions():
    print "functions"

def calculus():
    print "calculus"


def science():
    print "science"

def mystery():
    print "mystery"

def get_choices(paths, calling_function):
    number_of_choices = len(paths)
    choice = raw_input("\n> ")
    if choice.isdigit():
        choice = eval(choice)

        if choice >= 1 and choice <= number_of_choices:
            arch_room(paths[choice - 1])
        else:
            print "You entered a number, but it wasn't a choice."
            calling_function()
    else:
        print "Enter one of %s please. \n" % range(1, number_of_choices + 1)
        calling_function()

def green():
    print green_text % border
    categories = ['math', 'science', 'mystery', 'red']
    get_choices(categories,green)

def red():
    print "\n\nSadly, your adventure has come to an end.\n"





#Function calls

start()
