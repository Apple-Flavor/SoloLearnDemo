from unnecessary_math import multiply
from nose import with_setup

def my_setup_function():
    print "my_setup_function"

def my_teardown_function():
    print "my_teardown_function"

@with_setup(my_setup_function, my_teardown_function)
def test_numbers_3_4():
    print "test_numbers_3_4"
    assert multiply(3,4)==12
