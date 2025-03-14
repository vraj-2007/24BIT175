celsius=[20,25,30,10,15]
n=0
fahrenheit=[]
for fer in celsius:
    fer=int(9/5 * (celsius[n])+32)
    fahrenheit.append(fer)
    n+=1

print(fahrenheit)

#if we write short code
f_temperature=[(c* 9/5) + 32 for c in celsius]
print(f_temperature)
