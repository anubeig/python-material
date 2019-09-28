list1 = [1,3,2,4,5,2,1,2]
print(list1)
print(set(list1))

new_list = []
duplicate_list = []

for value in list1:
    if value not in new_list:
        new_list.append(value)
    else:
        if value not in duplicate_list:
            duplicate_list.append(value)

print(new_list)
print(duplicate_list)
