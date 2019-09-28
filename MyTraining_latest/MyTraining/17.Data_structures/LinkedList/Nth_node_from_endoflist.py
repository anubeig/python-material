"""
Method 2 (Use two pointers)
Maintain two pointers – reference pointer and main pointer.
Initialize both reference and main pointers to head.
First move reference pointer to n nodes from head.
Now move both pointers one by one until reference pointer reaches end.
Now main pointer will point to nth node from the end. Return main pointer.
"""
def printNthFromLast(self, n):
    main_ptr = self.head
    ref_ptr = self.head

    count = 0
    if (self.head is not None):
        while (count < n):
            if (ref_ptr is None):
                print "%d is greater than the no. pf \
                        nodes in list" % (n)
                return

            ref_ptr = ref_ptr.next
            count += 1

    while (ref_ptr is not None):
        main_ptr = main_ptr.next
        ref_ptr = ref_ptr.next

    print "Node no. %d from last is %d " % (n, main_ptr.data)