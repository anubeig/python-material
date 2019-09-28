import threading

a = 10

lock = threading.Lock()

def fun():
    global a
    lock.acquire()
    a +=1
    lock.acquire() # HANG FOR EVER BECAUSE an only be acquired once.
                   # It cannot be acquired again, until it is released. (After it's been released, it can be re-acaquired by any thread).
    lock.relase()
    lock.release()
    pass

t1 = threading.Thread(target=fun)
t1.start()

"""
output:-
sh-4.3$ python main.py
Acquired first time
                                    ====================>Hang forever
"""

import threading

a = 10

lock = threading.RLock()

def fun():
    global a
    lock.acquire()
    print "Acquired first time"
    a +=1
    lock.acquire()  # with RLock we can acquire twice
    print "Acquired second time"
    lock.release()
    print "Release second"
    lock.release()
    print "Release First"
    pass

t1 = threading.Thread(target=fun)
t1.start()
"""
output:-
sh-4.3$ python main.py
Acquired first time

Acquired second time
Release second
Release First
"""