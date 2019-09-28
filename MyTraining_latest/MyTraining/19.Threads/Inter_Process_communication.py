import time
import threading

loc = threading.Condition()


class bank():
    amount = 10000

    def withdraw(self, amount):
        loc.acquire()
        if self.amount < amount:
            print "Less balance waiting for deposit"
            loc.wait()
            self.amount = self.amount - amount
            print "Withdraw completed"
            print "Amount after withdraw: " + str(self.amount)
        loc.release()

    def deposit(self, amount):
        loc.acquire()
        print "goint to deposit"
        self.amount += amount
        print "deposited"
        loc.notify()
        loc.release()

    pass


class myThread1(threading.Thread):
    # t = None
    def __init__(self, t):
        threading.Thread.__init__(self)
        self.t = t

    def run(self):
        t.withdraw(12000)
        pass

    pass


class myThread2(threading.Thread):
    # t = None
    def __init__(self, t):
        threading.Thread.__init__(self)
        self.t = t

    def run(self):
        t.deposit(5000)
        pass

    pass


t = bank()

thread1 = myThread1(t)
thread2 = myThread2(t)

#loc.wait() throws following Runtimeerror
"""
 File "main.py", line 53, in <module>

    loc.wait()
  File "/usr/lib64/python2.7/threading.py", line 333, in wait
    raise RuntimeError("cannot wait on un-acquired lock")
RuntimeError: cannot wait on un-acquired lock
"""
loc.notify()
thread1.start()
thread2.start()

"""
sh-4.3$ python main.py
Less balance waiting for deposit
goint to deposit

deposited
Withdraw completed
Amount after withdraw: 3000
"""