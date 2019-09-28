#reverse a list based on nof repeating characters suppose [1,2,3,4,5], repeat 2 numbers then output should be [2,1,4,3,5]
n=2
list1 = [1,2,3,4,5]
print list1[n:]+list1[:n]