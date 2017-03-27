#ex36v2 - added get_choices function and changed the way text was generated
#ex36v3 - reorganized code, making function calls easier to read.
#ex36v4 - updated the arithmetic function to present 5 randomized questions! Added point system
#ex36v5 - updated the calculus function to include sympy support
#Imports
import random
from sympy import *
#Variables
points = 10
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

You have %d points.

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

You have %d points.

"""

arithmetic_text = """
%s
Very well young traveler. So far you have %d points. Each arithmetic question answered correctly
will grant you the specified number of points. Get it wrong, and you'll lose points.
Lose too many points and the game's over!

Now then, time to test your math arithemtic skills.
""" % (border, points)

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
    global points
    print math_text % (border, points)
    categories = ['arithmetic', 'functions', 'calculus','green', 'red']
    get_choices(categories,math)

def arithmetic():
    #print arithmetic_text
    level = 1
    question = 1
    question_text = "Probelm number %d out of 5: \n"
    print question_text % question
    value = arithmetic_problem(level)
    while question < 5:
        question += 1
        print question_text % question
        if value:
            level += 1
            value = arithmetic_problem(level)

        else:
            value = arithmetic_problem(level)
    math()


def arithmetic_problem(level):
    global points
    print "Level %d quesiton: " % level,
    numbers = [float(int(10  * random.random())) for i in xrange(level + 1)]
    operators = [generate_operator() for i in xrange(level)]
    numbers, operators = check_zeros(numbers, operators, level)
    calculation = combine_numbers_operators(numbers, operators)
    problem = ' '.join(map(str, calculation))
    print problem + ' = ? To 2 decimal places\n'
    user_answer = raw_input("> ")

    try:
        user_answer = float(user_answer)
        if user_answer == float("%.2f" % eval(problem)):
            print "Correct!"
            points += level
            print "You have %d points.\n" % points
            return True
        else:
            print "Incorrect! The answer was %f." % float("%.2f" % eval(problem))
            points -= level
            print "You have %d points.\n" % points
            return False
    except:
        print "Next time, try entering only numbers and a decimal."
        arithmetic_problem(level)

    # if operators.count('/') >= 1 and zeros >= 1:
    #     remove = zeros
    #     while remove > 0:
    #         numbers.remove(0)
    #         numbers.append(int(10 ** level * random.random()))
    #         remove -= 1
def check_zeros(numbers, operators, level):
    zeros = numbers.count(0)
    if operators.count('/') >= 1 and zeros >= 1:

        remove = zeros
        while remove > 0:
            numbers.remove(0)
            numbers.append(float(int(10  * random.random())))
            remove -= 1
    return [numbers, operators]
    #Testing random number generation
    # for i in range(1,10):
    #     for j in range(1,10):
    #         o = generate_operator()
    #         k = eval("%f %s %f" % (i,o,j))
    #         print "Now performing %d %s %d = %.2f" % (i,o,j,k)

def generate_operator():
    operators = ['+', '-', '*','/']
    operator = operators[random.randint(0,3)]
    return operator
def combine_numbers_operators(numbers, operators):
    length = len(numbers)

    i = 0
    combination = []
    while i < length - 1:
        combination.append(numbers[i])

        combination.append(operators[i])
        i += 1
    combination.append(numbers[i])
    return combination

def functions():
    print "functions"

def calculus():
    print "calculus"
    #print arithmetic_text
    level = 1
    question = 1
    question_text = "Probelm number %d out of 5: \n"
    print question_text % question
    value = calculus_problem(level)
    while question < 5:
        question += 1
        print question_text % question
        if value:
            level += 1
            value = arithmetic_problem(level)

        else:
            value = arithmetic_problem(level)
    math()

def calculus_problem(level):
    print "calculus problem"

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
    print green_text % (border, points)
    categories = ['math', 'science', 'mystery', 'red']
    get_choices(categories,green)

def red():
    print "\n\nSadly, your adventure has come to an end.\n"




#Function calls

start()
