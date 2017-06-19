import sys
err = sys.stderr

initialized = False

def setup_package():                   # or setup, setUp, or setUpPackage
    global initialized
    initialized = True

    err.write('PACKAGE SETUP\n')

def teardown_package():                # or teardown, tearDown, tearDownPackage
    global initialized
    initialized = False

    err.write('PACKAGE TEARDOWN\n')

def test_at_root():
    assert initialized

    err.write('PACKAGE: test_at_root\n')
