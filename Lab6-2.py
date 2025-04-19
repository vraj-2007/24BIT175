students = [
    (188, "nek", 20),
    (175, "vraj", 21),
    (173, "ved", 19),
    (186, "parva", 22)
]
roll_nos = []
names = []
ages = []
for student in students:
    roll_nos.append(student[0])
    names.append(student[1])     
    ages.append(student[2])      
print("Roll Numbers:", roll_nos)
print("Names:", names)
print("Ages:", ages)
