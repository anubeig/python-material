import threading
import time

class primeNumber(threading.Thread):
    def run(self):
        for index in range(5):
            print index
            time.sleep(3)
            pass
pass

t1 = primeNumber()
t2 = primeNumber()
t1.start()
#t1.start() ===================> Raise exception
"""
  File "/usr/lib64/python2.7/threading.py", line 742, in start
    raise RuntimeError("threads can only be started once")
RuntimeError: threads can only be started once
"""
t2.start()

"""
Output:-

sh-4.3$ python main.py
0
0
1
 1
2
2
3
3
4
4          
"""


