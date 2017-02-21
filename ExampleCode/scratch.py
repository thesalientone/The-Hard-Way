def fun1(name):
    name()

def math():
    print "Math works"

fun1(math)
print type(math)
