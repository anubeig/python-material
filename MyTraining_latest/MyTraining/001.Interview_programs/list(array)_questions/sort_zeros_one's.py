#sort 0's and 1's

list1 = [0,1,1,0,1,0]

zeros = list1.count(0)
print [0]*zeros+[1]*(len(list1)-zeros)

"""
output:-
[0, 0, 0, 1, 1, 1]
"""