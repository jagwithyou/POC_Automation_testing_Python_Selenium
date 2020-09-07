# content of test_sample.py
def func(x):
    return x + 1

def test_answer():
    ''' This is a simple test to check pytest '''
    assert func(3) == 4 