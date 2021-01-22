list1 = [12, -7, 5, 64, -14]
for a in list1 :
    if a > 0:
        print (a , end = ' ,')

list2 = [12, 14, -95, 3]
for i in list2:
    if i < 0 :
        list2.remove(i)
        print (list2)