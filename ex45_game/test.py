class ClassTest(object):

    var1 = 5
    def __init__(self):
        print "hello"

test1 = ClassTest()
test2 = ClassTest()

test1.var1 += 5

print test2.var1
print test1.var1


testdict = { 'a' : 5 }

print testdict['a']


def function1():

    return (5, 4)


x = function1()

print x[0]


dictionary1 = { 'a' : 5 , 'b' : 33 , 'c': 44, 'd' : ClassTest() }

ivd = { v : k for k, v in dictionary1.items()}

print ivd[5]


print ClassTest.var1
