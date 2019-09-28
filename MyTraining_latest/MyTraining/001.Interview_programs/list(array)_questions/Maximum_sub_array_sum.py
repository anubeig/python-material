#http://www.geeksforgeeks.org/largest-sum-contiguous-subarray/

# Python program to find maximum contiguous subarray

# Function to find the maximum contiguous subarray
from sys import maxint


def maxSubArraySum(a, size):
    max_so_far = -maxint - 1
    max_ending_here = 0

    for i in range(0, size):
        max_ending_here = max_ending_here + a[i]
        if (max_so_far < max_ending_here):
            max_so_far = max_ending_here

        if max_ending_here < 0:
            max_ending_here = 0
    return max_so_far


# Driver function to check the above function
a = [-13, -3, -25, -20, -3, -16, -23, -12, -5, -22, -15, -4, -7]
print "Maximum contiguous sum is", maxSubArraySum(a, len(a))


list = [4, -2, -8, 5, -2, 7, 7, 2, -6, 5]

def mssl(x):
    max_ending_here = max_so_far = 0
    for a in x:
        max_ending_here = max(0, max_ending_here + a)
        print max(0, max_ending_here + a)
        max_so_far = max(max_so_far, max_ending_here)
    return max_so_far