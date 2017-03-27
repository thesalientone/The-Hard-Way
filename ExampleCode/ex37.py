#Assert - ensure that something is true

#assert False, "Error!!"      Displays Error!! in terminal
#assert 5 == 5, "Text"        Doesn't display anything

#Break stops loop

for i in range(9):
    print "Number : %d" % i
    if i == 6:
        print "Stopping at 6"
        print "\n" * 4
        break

#Continue , starts loop over
j = 1
while j < 10:
    print "Number: %d" % j
    if j < 4:
        print "We add 2:"
        j += 2
        continue
    print "We dont't add 2, we add 1"
    j += 1

#del deletes entry from dictionary
tel = {'person1': 200 , 'person2': 300}
del tel['person2']
print tel

#exec runs string as python code

exec 'print "Hello"'

#finally runs code after a try statement after leaving try

# try:
#     raise KeyboardInterrupt
# finally:
#     print 'Goodbye, world!'

# pass  empty block of code, can be used as a place holder!
def test_function(arg):
    pass

#raise calls an exeption of the type specified (see finally above)
#
# with 5 as xyz:
#     print xyz
