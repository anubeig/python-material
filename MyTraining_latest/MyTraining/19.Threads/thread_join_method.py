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
t1.join()
"""
The join() method waits for a thread to die. In other words,
it causes the currently running threads to stop executing until the thread it joins with completes its task.
"""
t2.start()

"""
output:-
sh-4.3$ python main.py
0
1
2
3
4
0

1
2
3
"""


