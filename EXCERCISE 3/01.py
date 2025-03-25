a = float(input("Enter first number:"))
b = float(input("Enter second number:"))
if a>b:
    mx = a
    mn = b
else:
    mx = b
    mn = a
print("Largest number:", mx)
print("Smallest number:", mn)