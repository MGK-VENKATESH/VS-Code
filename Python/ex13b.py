def reverse_str(s):
    str=" "
    for i in s:
        str=i+str
    return str
s=input("enter the string do you want to reverse")
print("entered string is:")
print(s)
print("reversed strimg is:")
print(reverse_str(s))