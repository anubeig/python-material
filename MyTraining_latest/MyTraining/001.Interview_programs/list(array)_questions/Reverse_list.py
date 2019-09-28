#JP-Morgan chase interview question
#reverse a list based on nof repeating characters suppose [1,2,3,4,5], repeat 2 numbers then output should be [2,1,4,3,5]
list1 = [1, 2, 3, 4, 5]
noOfrepeats = 4
new_list = []
count = 0
for index in range(0, int(len(list1) / noOfrepeats)):
    start = count
    end = count + noOfrepeats
    l1 = list1[start:end]
    new_list = new_list + l1[::-1]
    count = count + noOfrepeats

new_list = new_list + list1[count:]

print(new_list)

#reverse a list based on nof repeating characters suppose [1,2,3,4,5], repeat 2 numbers then output should be [2,1,4,3,5]

list = [1, 2, 3, 4, 5]

def rev_groups(inp_list, n):
    lists = [inp_list[i:i+n] for i in range(0, len(inp_list), n)]
    print lists
    for lis in lists:
        lis.reverse()
    return lists

print rev_groups(list,2)

"""
output:-[[2, 1], [4, 3], [5]]
"""