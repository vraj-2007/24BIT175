import math
n=int(input("enter a number="))
factorial=math.factorial(n)
print("factorial","=",factorial)

#for loop

n=int(input("enter a number="))
fact=1
for i in range(1,n+1):
    fact*=i
print("factorial=",fact)