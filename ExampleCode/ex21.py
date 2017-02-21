def add(a, b):
    print "Adding %d + %d" % (a, b)
    return a + b

def subtract(a, b):
    print "Subtracting %d - %d" % (a, b)
    return a - b

def multiply(a, b):
    print "Muliplying %d x %d" % (a, b)
    return a * b

def divide(a,b):
    print "Dividing %d / %d" % (a, b)
    return a / b

print "Let's do some math with just funcitons!"

age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print "Age: %d, Height: %d, Weight: %d, Iq: %d" % (age, height, weight, iq)

#A puzzle for the extra credit, type it in anyway
def whatformula(a,b,c,d):
    print "%d minus (%d times %d) divided by 2 + %d" % (a, b, c, d)
    return a - ((b * c) / 2) + d

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print "That becomes: ", what, "Can you do it by hand?"
print whatformula(height, iq, weight, age)
