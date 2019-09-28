#http://www.geeksforgeeks.org/detect-loop-in-a-linked-list/
#Detect a loop in a linked list

def detectLoop(self):
    slow_p = self.head
    fast_p = self.head
    while (slow_p and fast_p and fast_p.next):
        slow_p = slow_p.next
        fast_p = fast_p.next.next
        if slow_p == fast_p:
            print "Found Loop"
            return