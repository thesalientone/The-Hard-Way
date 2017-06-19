###
### basic attribute stuff -- 'will_fail' is a property on each test, and
### you can test for its truth or its existence.
###
### with '-a !will_fail', testme1 and testme3 are run;
### with '-a will_fail', testme2 is run;
### with '-a will_fail=False', testme1 is run.
###

def testme1():
    assert 1

testme1.will_fail = False

def testme2():
    assert 0

testme2.will_fail = True

def testme3():
    assert 1
