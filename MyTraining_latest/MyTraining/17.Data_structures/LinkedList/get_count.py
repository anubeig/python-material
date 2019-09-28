# This function counts number of nodes in Linked List
# iteratively, given 'node' as starting node.
def getCount(self):
    temp = self.head  # Initialise temp
    count = 0  # Initialise count

    # Loop while end of linked list is not reached
    while (temp):
        count += 1
        temp = temp.next
    return count