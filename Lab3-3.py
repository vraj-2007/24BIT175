string=input("enter string:")
alph=0
dig=0
for char in string:
    if char.isalpha():
        alph+=1
    elif char.isdigit():
        dig+=1
print("no. of alphabets in string=",alph)
print("no. of digits in string=",dig)