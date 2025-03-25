import random
l = []
for i in range(30):
    n = random.randint(-50, 50)
    l.append(n)
print("Original list:", l)
pos = []
neg = []
for n in l:
    if n >= 0:
        pos.append(n)
    else:
        neg.append(n)
print("Positive numbers:", pos)
print("Negative numbers:", neg)