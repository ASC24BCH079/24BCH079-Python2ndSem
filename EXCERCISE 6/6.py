n = (11, 12, 13, 14, 15, 16, 17, 18, 19, 20)
i = 1
v = 25
n = n[:i] + (v,) + n[i+1:]
print("Tuple after modifying element at index", i, ":", n)
