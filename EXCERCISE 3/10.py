l = float(input("Enter length of rectangle:"))
b = float(input("Enter breadth of rectangle:"))
a = l*b
p = (l+b)*2
if a>p:
    print("Area is greater than perimeter")
else:
    print("Area isn't greater than perimeter")