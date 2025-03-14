odd_numbers = [int(input("enter odd numbers="))for _ in range(5)]
even_numbers = [int(input("enter even numbers="))for _ in range(4)]
print("odd numbers:",odd_numbers)
print("even numbers:",even_numbers)
odd_numbers[2]=even_numbers
print("list after replace=",odd_numbers)

flattened_list = []
for item in odd_numbers:
    if type(item)==list:
        for num in item:
            flattened_list.append(num)
    else:
        flattened_list.append(item)
print("flattened list:",flattened_list)
flattened_list.sort()
print("sorted list:",flattened_list)

