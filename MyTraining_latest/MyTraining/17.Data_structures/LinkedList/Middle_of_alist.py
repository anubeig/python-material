#Middle of a list

def MiddleOfAList(self):
    slow_p = self.head
    fast_p = self.head
    while (fast_p and fast_p.next):
        slow_p = slow_p.next
        fast_p = fast_p.next.next
    print "The middle element is "+slow_p.data