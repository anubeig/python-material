#http://www.geeksforgeeks.org/add-two-numbers-represented-by-linked-lists/
"""
Input:
  First List: 5->6->3  // represents number 365
  Second List: 8->4->2 //  represents number 248
Output
  Resultant list: 3->1->6  // represents number 613


  Solution
Traverse both lists. One by one pick nodes of both lists and add the values.
If sum is more than 10 then make carry as 1 and reduce sum.
If one list has more elements than the other then consider remaining values of this list as 0.
Following is the implementation of this approach.
"""


# Add contents of two linked lists and return the head
# node of resultant list
def addTwoLists(self, first, second):
    prev = None
    temp = None
    carry = 0

    # While both list exists
    while (first is not None or second is not None):

        # Calculate the value of next digit in
        # resultant list
        # The next digit is sum of following things
        # (i) Carry
        # (ii) Next digit of first list (if ther is a
        # next digit)
        # (iii) Next digit of second list ( if there
        # is a next digit)
        fdata = 0 if first is None else first.data
        sdata = 0 if second is None else second.data
        Sum = carry + fdata + sdata

        # update carry for next calculation
        carry = 1 if Sum >= 10 else 0

        # update sum if it is greater than 10
        Sum = Sum if Sum < 10 else Sum % 10

        # Create a new node with sum as data
        temp = Node(Sum)

        # if this is the first node then set it as head
        # of resultant list
        if self.head is None:
            self.head = temp
        else:
            prev.next = temp

            # Set prev for next insertion
        prev = temp

        # Move first and second pointers to next nodes
        if first is not None:
            first = first.next
        if second is not None:
            second = second.next

    if carry > 0:
        temp.next = Node(carry)


# Utility function to print the linked LinkedList
def printList(self):
    temp = self.head
    while (temp):
        print temp.data,
        temp = temp.next
