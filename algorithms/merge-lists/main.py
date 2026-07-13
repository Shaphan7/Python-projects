def merge(list_1, list_2):
    list_3 = []
    while list_1 and list_2:
        if list_1[0] < list_2[0]:
            list_3.append(list_1[0])
            list_1.pop(0)
        elif list_2[0] < list_1[0]:
            list_3.append(list_2[0])
            list_2.pop(0)
        else:
            list_3.append(list_1[0])
            list_3.append(list_2[0])
            list_1.pop(0)
            list_2.pop(0)
    list_3.extend(list_1)
    list_3.extend(list_2)

    return list_3
    
print(merge([1,3,5],[2,4]))
