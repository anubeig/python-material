


#Need to investigate more on this topic

import time

if __name__ == '__main__':
    start = time.clock()
    for x in range (1, 100):
        dog = "a" + "b" + "c" + "d" +"e"

    end = time.clock()
    print "Time to run Plusser = ", end - start, "seconds"
print dog

import time
if __name__ == '__main__':
    start = time.clock()
    for x in range (1, 100):
        dog = "".join(["a","b","c","d","e"])
    print dog
    end = time.clock()
    print "Time to run Joiner = ", end - start, "seconds"