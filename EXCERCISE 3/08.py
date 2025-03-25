a = float(input("Enter first angle:"))
b = float(input("Enter second angle:"))
c = float(input("Enter third angle:"))
s = a+b+c
if s == 180:
    print("Triangle is valid")
else:
    print("Triangle is invalid")