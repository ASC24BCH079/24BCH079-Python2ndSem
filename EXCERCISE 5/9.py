l1 = [10, 20, 30, 40, 50]
l2 = [15, 20, 25, 30, 35, 40]

print("First list:", l1)
print("Second list:", l2)

l3 = []
for num in l1:
    if num not in l2:
        l3.append(num)

print("Numbers in first list not in second list:", l3)