list1=[1,2,3,4,5]
list2=[4,5,6,7,8]
list3=[]
for num in list1:
    if num not in list2:
        list3.append(num)

print("list1=",list1)
print("list2=",list2)
print("list3=",list3)

#using list comprehension

unique_list=[num for num in list1 if num not in list2]

print("unique list=",unique_list)