a = int(input("Enter size in Bytes: "))
x = a/1024
y = x/1024
z = y/1024
print(f"{a} Bytes are equal to:\n{round(x, 2)} KB\n{round(y, 2)} MB\n{round(z, 2)} GB.")