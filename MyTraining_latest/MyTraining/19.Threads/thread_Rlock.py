The main difference is that a Lock can only be acquired once. It cannot be acquired again, until it is released. (After it's been released, it can be re-acaquired by any thread).

An RLock on the other hand, can be acquired multiple times, by the same thread. It needs to be released the same number of times in order to be "unlocked".

Another difference is that an acquired Lock can be released by any thread, while an acquired RLock can only be released by the thread which acquired it.

Here's an example demostrating why RLock is useful at times. Suppose you have:

def f():
  g()
  h()

def g():
  h()
  do_something1()

def h():
  do_something2()
Let's say all of f, g, and h are public (i.e. can be called directly by an external caller), and all of them require syncronization.

Using a Lock, you can do something like:

lock = Lock()

def f():
  with lock:
    _g()
    _h()

def g():
  with lock:
    _g()

def _g():
  _h()
  do_something1()

def h():
  with lock:
    _h()

def _h():
  do_something2()
Basically, since f cannot call g after acquiring the lock, it needs to call a "raw" version of g (i.e. _g). So you end up with a "synced" version and a "raw" version of each function.

Using an RLock elegantly solves the problem:

lock = RLock()

def f():
  with lock:
    g()
    h()

def g():
  with lock:
    h()
    do_something1()

def h():
  with lock:
    do_something2()