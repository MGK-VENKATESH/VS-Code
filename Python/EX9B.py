def dups(list):
    for i in list:
        count=list.count(i)
        if count>1:
            print("there are duplicates")
        else:
            print("there are no duplicates")
a=[8,6,4,7,8,9]
b=[5,6,7,8,9]
dups(a)
dups(b)