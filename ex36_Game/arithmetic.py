import random
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


def arithmetic_problem(level):
    print "Level %d quesiton: " % level,
    numbers = [float(int(10 ** level * random.random())) for i in xrange(level + 1)]
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
            return True
        else:
            print "Incorrect! The answer was %f." % eval(problem)
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
            numbers.append(float(int(10 ** level * random.random())))
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


def operate(a,b,operation):
    print "What is %d %s %d = ?\n" % (a, operation, b)
    k = eval("%f %s %f" % (a, operation, b))
    answer = raw_input("> ")
    if answer.isdigit():
        answer = float(eval(answer))
        if answer == k:
            print "Correct."
            return True
        else:
            print "Incorrect. The answer was %f." % k
            return False
    else:
        print "Enter a number please."
        operate(a,b,operation)

arithmetic()
# for i in range(1,4):
#     arithmetic_problem(i)
