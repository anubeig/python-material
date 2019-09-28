def bubble_sort(aList):
    for numberPass in range(len(aList)):
        for i in range(0,len(aList)-numberPass-1):   # Note after each pass the maximum value will be placed
            if aList[i]>aList[i+1]:
                temp = aList[i]
                aList[i] = aList[i+1]
                aList[i+1] = temp
    return aList

print bubble_sort([6,3,7,21,2,5])
