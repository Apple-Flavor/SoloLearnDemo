import time
import os
import timeout_decorator

@timeout_decorator.timeout(5)
def func(t):
    print "=== Start"
    time.sleep(t)
    os.system("top")
    print "====Stop"

if __name__ == '__main__':
    try:
        func(10)
    except:
        pass
    try:
        func(10)
    except:
        pass
