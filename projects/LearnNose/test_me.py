import unittest
def test_b():
    assert 'b' == 'b'

class TestExampleTwo:
    def test_c(self):
        assert 'c' == 'c'

    def test_another(self):
        assert self.__class__ == TestExampleTwo

    #def test_failthis(self):
    #    assert self.__class__.__name__ == 'Test'

    def test_noassert(self):
        x = 5
        return x

class ExampleTest(unittest.TestCase):
    def test_a(self):
        self.assert_(1 == 1)
