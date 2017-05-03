class MonsterTest(object):
    def __init__(self, var):
        self.var = var
        print "Made var"



Mob = MonsterTest(5)
class_to_make = Mob.__class__

a = MonsterTest

b = a(4)


i = [5]
k = 0

while i:
    print "There is still an i. k = %d" % k
    k += 1

    if k == 20:
        i.pop(0)
        print "No more i"

dictionary = {b : 'hello'}
print dictionary.keys()
print dictionary[b]
