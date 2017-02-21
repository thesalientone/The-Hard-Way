#This initialzies a variable x to a string
x = "There are %d types of people." % 10
#This initializes a varialbe binary to a string
binary = "binary"
#This initializes a variable do_not to a string
do_not = "don't"
#This initializes a variable y to a string containing specifiers and their formats
y = "Those who know %s and those who %s." % (binary, do_not)
#This prints x
print x
#This prints y
print y
#This prints a string using x as input
print "I said: %r." % x
#This prints a string using y as input
print "I also said: '%s'." % y
#This initializes a variable hilarious with the value False
hilarious = False
#This initializes a variable joke_evaluation with a string with a specifier but lacking the argument
joke_evaluation = "Isn't that joke so funny?! %r"
#This prints a string using hilarious as an argument to joke_evaluation
print joke_evaluation % hilarious
#This initializes a variable w with a string
w = "This is the left side of ..."
#This initializes a variable e with a string
e = "a string with a right side."
#This prints the results of adding strings w and e together
print w + e
