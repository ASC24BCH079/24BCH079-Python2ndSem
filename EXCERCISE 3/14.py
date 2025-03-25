s1 = float(input("Enter marks for subject 1: "))
s2 = float(input("Enter marks for subject 2: "))
s3 = float(input("Enter marks for subject 3: "))
t = s1+s2+s3
a = t/3
if s1<=39 or s2<=39 or s3<=39:
    r = "Fail"
else:
    r = "Pass"

print("Result:", r)

if a >= 80:
    g = "O"
elif a >= 70:
    g = "A+"
elif a >= 60:
    g = "A"
elif a >= 55:
    g = "B+"
elif a >= 50:
    g = "B"
elif a >= 45:
    g = "C"
elif a >= 40:
    g = "P"
else:
    g = "F"
print("Total marks:", t)
print("Average marks:", round(a, 2))
print("Grade:", g)