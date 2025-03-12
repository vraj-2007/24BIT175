num=int(input("enter number of terms="))
if num <=0:
    print("none")
elif num==1:
    print("fibbonacci sequence= [0]")
else:
    fib_sequence=[0,1]
    for i in range(2,num):
        fib_sequence.append(fib_sequence[i-1]+fib_sequence[i-2])
print("fibbonacci sequence:",fib_sequence)