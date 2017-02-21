from sys import argv

script, first, second = argv

print "The first variable is: ", first
print "The second variable is: ", second

third = raw_input("Any other input? : ")

if third != "":
    print "The third varialbe is: ", third
