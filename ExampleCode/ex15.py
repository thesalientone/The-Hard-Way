#Imports the arguments used to call the script from the system module
from sys import argv
#Assigns variable names to the arguments
script, filename = argv
#Opens a file and assigns it txt
txt = open(filename)
#Prints the name of the file
print "Here's your file %r:" % filename
#Prints the contents of the file contained in txt
print txt.read()

txt.close()
#Prints a string
print "Type the filename again:"
#Asks the user to input a file name and stores it as file_again
file_again = raw_input("> ")
#Opens the file name specified by the user
txt_again = open(file_again)
#Prints the text of that file
print txt_again.read()
txt_again.close()
