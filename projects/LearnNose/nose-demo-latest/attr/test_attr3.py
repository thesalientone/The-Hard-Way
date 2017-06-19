###
### attributes on classes
###

class TestMe:
    x = True
    y = False

    def test_case1(self):
        assert 1

    def test_case2(self):
        assert 1
        
    test_case2.x = False
    test_case2.y = True
