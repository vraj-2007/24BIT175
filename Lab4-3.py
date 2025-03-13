string1=input("enter first string=")
string2=input("enter second string=")
if string1 in string2:
    print("first string in second string")
elif string2 in string1:
    print("second string in first string")
else:
    print("fisrt string not in second string",".second string not in first string")

