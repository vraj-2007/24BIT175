from datetime import date
date1 = (10, 7, 2007) 
date2 = (15, 7, 2007)
d1 = date(date1[2], date1[1], date1[0])
d2 = date(date2[2], date2[1], date2[0])
difference = abs((d2 - d1).days)
print("Number of days between the two dates:", difference)
