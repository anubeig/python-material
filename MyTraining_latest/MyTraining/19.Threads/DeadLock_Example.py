import thread
import time
import threading

a = "I am string1"
b = "I am string2"
lock1 = threading.Lock()
lock2 = threading.Lock()


class myThread1(threading.Thread):
    def run(self):
        global a, b
        lock1.acquire()
        print "Thread 1: locked resource a"
        a += "adding synch"
        time.sleep(5)

        lock2.acquire()
        print "Thread 1: locked resource b"
        b += "adding synch"
        time.sleep(5)
        lock2.release()
        lock1.release()
        pass

    pass

class myThread2(threading.Thread):
    def run(self):
        global a, b
        lock2.acquire()
        print "Thread 2: locked resource b"
        b += "adding synch"
        time.sleep(5)

        lock1.acquire()
        time.sleep(5)
        print "Thread 2: locked resource a"
        a += "adding synch"
        lock1.release()
        lock2.release()
        pass

    pass


thread1 = myThread1()
thread2 = myThread2()

thread1.start()
thread2.start()

"""
output:-
sh - 4.3$ python
main.py
Thread 1: locked resource a
Thread 2: locked resource b
"""