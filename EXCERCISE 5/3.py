import random
l = []
for i in range(50):
    n = random.randint(1, 30)
    l.append(n)
print("Original list:", l)
nd = []
for n in l:
    if n not in nd:
        nd.append(n)
print("List after removing duplicates:", nd)