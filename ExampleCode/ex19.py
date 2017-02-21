#Defines a function named cheese_and_crackers with 2 varibales as input
def cheese_and_crackers(cheese_count, boxes_of_crackers):
        #Prints a string with a variable input
        print "You have %d cheeses!" % cheese_count
        #Prints a string with a variable input
        print "You have %d boxes of crackers" % boxes_of_crackers
        #Prints a string
        print "Man that's enough for a party!"
        #Prints a string
        print "Get a blanket.\n"

#Prints a string
print "We can just give the function numbers directly:"
#Calls cheese_and_crackers with inputs of 20, 30
cheese_and_crackers(20,30)

#Prints a string
print "OR, we can use variables from our script:"
#Initializes a varialbe named amount_of_cheese to 30
amount_of_cheese = 10
#Initializes a variable named amount_of_crackers to 50
amount_of_crackers = 50
#Calls cheese_and_crackers with variable inputs
cheese_and_crackers(amount_of_cheese, amount_of_crackers)
#Prints a string
print "We can even do math inside too:"
#Calls cheese_and_crackers with inputs containing arithmetic
cheese_and_crackers(10 + 20, 5 + 6)
#Prints a string
print "And we can combine the two, variables and math:"
#Calls cheese_and_crackers with inputs contianing variables and arithmetic
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)

def cheese_volume(crackers_per_box, boxes_of_crackers):
    print "You have %d crackers per box, and %d boxes of crackers." % (crackers_per_box, boxes_of_crackers)
    print "You therefore have %d crackers" % (crackers_per_box * boxes_of_crackers)

cheese_volume(100, 50)

print "Wow you can repeat functions with a multiplication sign?\n" * 50
print "That's very useful!"
