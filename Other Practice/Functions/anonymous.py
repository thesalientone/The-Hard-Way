#Example of anonymous function using name = lamda [args]: f(args)

#Single variable

triple = lambda x: x * 3

print triple(7)
#Two input variables
binomial = lambda x,y: (x + y) ** 2

print binomial(2,5)


#filter() takes in a function and a list as arguments,
#returns a list containing all elements for whihch the function evaluates as true

my_list = range(0,101, 5)

new_list = list(filter(lambda x: (x % 2 == 0), my_list))

#print filter(lambda x: x % 2 == 0, my_list)

#map(function,list) returns a list that maps each element to a list containing
#each element evaluated by the function

my_list_2 = range(1,11)
func_2 = lambda x: x ** 2 # x squared
new_list_2 = map(func_2, my_list_2)

print my_list_2
print new_list_2
