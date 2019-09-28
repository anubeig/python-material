list1 = [1,0,3,0,3,4,5,0]
list2 = []
count = 0
for index in range(0,len(list1)):
        if list1[index] != 0:
            print("Non-zero")
            list2.append(list1[index])
        else:
            count +=1

list2 = list2+[0]*count
print(list2)

