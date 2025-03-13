string=input("enter string=")
vowels="AEIOUaeiou"
count=0
for i in string:
    if i in vowels:
       count+=1
print("total vowels in string=",count)