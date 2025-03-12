import math
n=int(input("enter n="))
r=int(input("enter r="))
a=math.factorial(n)
b=math.factorial(r)
c=math.factorial(n-r)
ncr=(a)/a*b
print("ncr","=",ncr)
npr=(a)/c
print("npr","=",npr)

