###
### attribute lists and sets
###
### basic stuff:
###
###   'nosetests -a tags=a' will run both testme5 and testme6
###   'nosetests -a tags=b' will run only testme5
###   'nosetests -a tags=c' will run only testme6
###   'nosetests -a tags=b,tags=c' will run neither.
###   'nosetests -a tags=b -a tags=c' will run both.
###
###

def testme5():
    assert 1

testme5.tags = ['a', 'b']

def testme6():
    assert 1
    
testme6.tags = ['a', 'c']
