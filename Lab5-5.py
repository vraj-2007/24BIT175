list=["apple","vraj","patel","hii","bheem"]
capitalized_list=[word.upper() for word in list]

print("list=",list)
print("capitalized list=",capitalized_list)

#if we use simple loop

capitalized_word=[]
for list1 in list:
    capitalized_word.append(list1.upper())

print("list=",list)
print("capitalized string=",capitalized_word)
