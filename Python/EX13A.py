n=int(input("enter the length of list"))
lst=[]
for i in range(0,n):
    element=int(input("enter the element"))
    lst.append(element)
def check_even(i):
    lst1=[]
    for i in range(0,n):
        lst1.append("true" if i%2==0 else "false")
        print(lst1)
check_even(lst)