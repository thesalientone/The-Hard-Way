import inspect
def multipleargs(*arg):
    print "I was called with %d arguments: %r" % (len(arg) ,arg)


multipleargs(*range(10))

def multiple_arg_parameters(*arg):
    for parameter in arg:
        print "Parameter number %d: %r" % (arg.index(parameter) , parameter)



multiple_arg_parameters(*range(5,20))

def multiple_keworded_args(**kwarg):

    for k, v in kwarg.items():
        print "The key %r has value %r" % (k, v)


multiple_keworded_args(target = 5, pulse = 'bomb')

class TestClass(object):

    def __init__(self, **kwargs):

        #for k, v in kwargs.iteritems():
        #    evalcode = 'self.%s = v' % str(k)
        #    exec(evalcode)
        #
        # if kwargs['target']:
        #     self.target = kwargs['target']
        # self.age = kwargs['age']
        # self.height = kwargs['height']
        self.__dict__.update(kwargs)
        self.att1 = Attribute('cure')
        self.att2 = Attribute('fire')


class Attribute(object):
    def __init__(self, name):
        self.name = name
    def printname(self):
        print self.name
    def __repr__(self):
        return "I am a class with name %s" % self.name

instance = TestClass(age = 20, height = 10, target = 'text')

b = Attribute("Billy")

class A(object):
    pass

print dir(A)
