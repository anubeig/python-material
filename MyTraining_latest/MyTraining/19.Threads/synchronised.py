import thread
import time
import threading

lock = threading.Lock()

class Table():
    def printTable(self, n):
        lock.acquire()
        for index in range(6):
            print n*index
            time.sleep(3)
        lock.release()
    pass

class myThread1(threading.Thread):
    #t = None
    def __init__(self,t):
        threading.Thread.__init__(self)
        self.t = t
    def run(self):
        t.printTable(1)
        pass
    pass

class myThread2(threading.Thread):
    #t = None
    def __init__(self,t):
        threading.Thread.__init__(self)
        self.t = t
    def run(self):
        t.printTable(100)
        pass
    pass

t = Table()

thread1 = myThread1(t)
thread2 = myThread2(t)

thread1.start()
thread2.start()

"""
output: without lock ( i.e if we commented out lock statements)
sh-4.3$ python main.py
0
 0

1
100
2
200
3
 300
4
400
5
 500


output: with lock
sh-4.3$ python main.py
0
1
2
3
4
5
0
100
200
300
400
500
"""

"""
If you declare any method as synchronized, it is known as synchronized method.

Synchronized method is used to lock an object for any shared resource.

When a thread invokes a synchronized method,
it automatically acquires the lock for that object and releases it when the thread completes its task.
"""