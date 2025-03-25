a = float(input("Enter first number:"))
b = float(input("Enter second number:"))
c = float(input("Enter third number:"))
if a>=b and a>=c:
    mx = a
elif b>=a and b>=c:
    mx = b
else:
    mx = c
if a<=b and a<=c:
    mn = a
elif b<=a and b<=c:
    mn = b
else:
    mn = c
print("Largest number:", mx)
print("Smallest number:", mn)