# Python program to detect and remove loop

"""
. After detecting the loop,
if we start slow pointer from head and move both slow and fast pointers at same speed until fast don’t meet,
they would meet at the beginning of linked list.

So if we start moving both pointers again at same speed such that one pointer (say slow) begins from head node of linked list and
other pointer (say fast) begins from meeting point.
 When slow pointer reaches beginning of linked list (has made m steps).
  Fast pointer would have made also moved m steps as they are now moving same pace. Since m+k is a multiple of n and fast starts from k,
they would meet at the beginning.
Can they meet before also? No because slow pointer enters the cycle first time after m steps.
"""
# Node class
class Node:
    # Constructor to initialize the node object
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    # Function to initialize head
    def __init__(self):
        self.head = None

    # Function to insert a new node at the beginning
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def detectAndRemoveLoop(self):
        slow = self.head
        fast = self.head.next

        # Search for loop using slow and fast pointers
        while (fast is not None):
            if fast.next is None:
                break
            if slow == fast:
                break
            slow = slow.next
            fast = fast.next.next

        # if loop exists
        if slow == fast:
            slow = self.head
            while (slow != fast.next):
                slow = slow.next
                fast = fast.next

            # Sinc fast.next is the looping point
            fast.next = None  # Remove loop

    # Utility function to print the linked LinkedList
    def printList(self):
        temp = self.head
        while (temp):
            print temp.data,
            temp = temp.next


# Driver program
llist = LinkedList()
llist.head = Node(50)
llist.head.next = Node(20)
llist.head.next.next = Node(15)
llist.head.next.next.next = Node(4)
llist.head.next.next.next.next = Node(10)

# Create a loop for testing
llist.head.next.next.next.next.next = llist.head.next.next

llist.detectAndRemoveLoop()

print "Linked List after removing looop"
llist.printList()