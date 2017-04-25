if 4 in  [4, 5, 6]:
    print 'yes'

if "hello" not in ["hello world", "hello"]:
    print "it's not"

class warrior(object):

    sword = "test"


john = warrior()
betty = warrior()

betty.sword = "ing"

print john.sword,
print betty.sword
