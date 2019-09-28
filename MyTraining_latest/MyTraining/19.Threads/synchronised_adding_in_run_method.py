import thread
import time
import threading

lock = threading.Lock()

class Table():
    def printTable(self, n):
        #lock.acquire()
        for index in range(6):
            print n*index
            time.sleep(3)
        #lock.release()
    pass

class myThread1(threading.Thread):
    #t = None
    def __init__(self,t):
        threading.Thread.__init__(self)
        self.t = t
    def run(self):
        lock.acquire()
        t.printTable(1)
        lock.release()
        pass
    pass

class myThread2(threading.Thread):
    #t = None
    def __init__(self,t):
        threading.Thread.__init__(self)
        self.t = t
    def run(self):
        lock.acquire()
        t.printTable(100)
        lock.release()
        pass
    pass

t = Table()

thread1 = myThread1(t)
thread2 = myThread2(t)

thread1.start()
thread2.start()

"""
output:-
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