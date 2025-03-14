import random

numbers=[random.randint(-50,50) for _ in range(30)]
print("total numbers=",numbers)
 
positive_numbers=[]
negative_numbers=[]
zero=[]

for nums in numbers:
    if nums>0:
        positive_numbers.append(nums)
    elif nums<0:
        negative_numbers.append(nums)
    else:
        zero.append(nums)
print("positive numbers=",positive_numbers)
print("negative numbers=",negative_numbers)

