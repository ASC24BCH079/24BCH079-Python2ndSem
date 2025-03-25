f = [92, 128, 86, 104, 212]
c = []
for k in f:
    s = (k-32)*5/9
    c.append(s)
print("Fahrenheit temperatures:", f)
print("Celsius temperatures:", c)