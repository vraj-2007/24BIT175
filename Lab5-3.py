import random
numbers=[random.randint(1,30) for _ in range(50)]
print("list=",numbers)
unique_number = list(set(numbers))
list1=list(unique_number)
print("list without duplicate=",list1)

#using loop
numbers=[random.randint(1,30) for _ in range(50)]
print("list=",numbers)
list1=[]
for num in numbers:
    if num not in list1:
        list1.append(num)
list1.sort()
print("list without duplicates=",list1)


