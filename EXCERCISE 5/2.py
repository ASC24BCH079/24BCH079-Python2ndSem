import random
l = []
for i in range(20):
    n = random.randint(1, 100)
    l.append(n)
print("List of random integers:", l)
num = int(input("Enter a number to search: "))
pos = []
for i in range(len(l)):
    if l[i] == num:
        pos.append(i)
if pos:
    print("Number found at position:", pos)
else:
    print("Number is not found in list")