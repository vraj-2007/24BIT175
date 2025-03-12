hour=24
for i in range(24):
    if i==0:
        print("12:00 midnight")
    elif i==12:
        print("12:00 noon")
    elif i<12:
        print(i,":AM")
    elif i>12:
        print(i-12,":PM")  
