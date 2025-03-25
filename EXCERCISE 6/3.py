from datetime import date
d1 = (25,10,2025)
d2 = (11,11,2025)
diff = (date(d2[2],d2[1],d2[0]) - date(d1[2],d1[1],d1[0])).days
print("Date 1:", d1)
print("Date 2:", d2)
print("Number of days between dates:", diff)