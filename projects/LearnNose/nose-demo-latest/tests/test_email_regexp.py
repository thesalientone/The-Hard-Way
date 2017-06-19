import re

EMAIL_REGEXP = re.compile(r'[\S.]+@[\S.]+')

def is_match(addr):
    return EMAIL_REGEXP.match(addr)

def test_normal():
    assert is_match('test@nowhere.com')
    assert is_match('AbraCaDaBra@Somewhere.It')

def test_fail():
    assert not is_match('test@')
    assert not is_match('@nowhere.com')
