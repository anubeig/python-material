import threading, time

a = 5
alock = threading.Lock()
b = 5
block = threading.Lock()

def thread1calc():
    global a,b
    print "Thread1 acquiring lock a"
    alock.acquire()
    time.sleep(5)

    print "Thread1 acquiring lock b"
    block.acquire()
    time.sleep(5)
    a += 5
    b += 5

    print "Thread1 releasing both locks"
    block.release()
    alock.release()

def thread2calc():
    global a,b
    print "Thread2 acquiring lock a"
    alock.acquire()
    
    print "Thread2 acquiring lock b"
    block.acquire()
    time.sleep(5)

    time.sleep(5)
    a += 10
    b += 10

    print "Thread2 releasing both locks"
    block.release()
    alock.release()

t = threading.Thread(target = thread1calc)
t.setDaemon(1)
t.start()

t = threading.Thread(target = thread2calc)
t.setDaemon(2)
t.start()

print "hello"
while 1:
    # Sleep forever
    time.sleep(300)
