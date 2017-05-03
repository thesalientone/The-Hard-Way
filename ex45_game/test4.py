time_table = range(1,10)
index = 0
for i in time_table:

    time_table[index] -= 1
    if time_table[index] == 0: print "Made it"
    index  += 1
print time_table


def testfunc():
    return 'a', 'b', 'c'

d, e, f = testfunc()

print d, e, f

test = raw_input('enter it')

if not test:
    print "no test"

x = ['cat', 'dog', 'rabbit']
if 'cat' in (x or ['woof', 'ribbit']):
    print "meow"

if 'cat' or 'dog' in x:
    print 'wow'

towns = ['town1']
prev_scene = 'start'
next_scene_name = 'field_0_1'

if prev_scene not in (towns  and ['open', 'start', 'menu']):
    print "It's not there"

class A(object):
    pass

z = A()

if z.__class__ == A:
    print "It's an A"

def localvars():
    a = 5
    b = 10
    c = 'string'
    print locals()
print locals()
localvars()
