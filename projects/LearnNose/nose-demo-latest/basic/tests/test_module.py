import sys
err = sys.stderr

initialized = False

###
### fixture functions -- run before (setup_module) and after (teardown_module)
### all tests in this module.
###

def setup_module():                     # or 'setup', 'setUp', 'setUpModule'
    global initialized
    initialized = True

    err.write('MODULE SETUP\n')

def teardown_module():                  # or 'teardown', 'tearDownModule'
    global initialized
    initialized = False

    err.write('MODULE TEARDOWN\n')

###
### the actual test(s).
###

# function-level tests

def test_me():
    assert initialized

def test_me_2():
    assert initialized

# class test; need not inherit from unittest.TestCase.

class TestClass:
    def __init__(self):
        self.cls_initialized = False

    ### fixtures again -- run before & after each test in this class.
    
    def setUp(self):
        assert not self.cls_initialized
        self.cls_initialized = True

        err.write('CLASS SETUP\n')

    def tearDown(self):
        assert self.cls_initialized
        self.cls_initialized = False

        err.write('CLASS TEARDOWN\n')

    ### actual tests.

    def test_1(self):
        err.write('CLASS TEST_1\n')

    def test_2(self):
        err.write('CLASS TEST_2\n')

###
### you can also have function tests with setup/teardown functions attached:
###

def _a():
    err.write('FN COMPLEX SETUP\n')

def _b():
    err.write('FN COMPLEX TEARDOWN\n')

def test_complex():
    err.write('FN COMPLEX TEST\n')

test_complex.setup = _a
test_complex.teardown = _b

###
### test function that returns a generator
###

# validation function
def check_sum(a, b, c):
    assert a+b == c

def test_check_sum():
    for i in range(0, 5):
        yield check_sum, i, i + 1, 2*i + 1
