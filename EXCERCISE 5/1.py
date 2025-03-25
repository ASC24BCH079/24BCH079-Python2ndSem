import random
odd = []
for i in range(5):
    n = random.randint(1, 100) * 2 - 1
    odd.append(n)
print("List of odd integers:", odd)
even = []
for i in range(4):
    n = random.randint(1, 50) * 2
    even.append(n)
print("List of even integers:", even)
odd[2] = even
print("List after replacing third element:", odd)
flat = []
for e in odd:
    if isinstance(e, list):
        for i in e:
            flat.append(i)
    else:
        flat.append(e)
print("Flattened list:", flat)
