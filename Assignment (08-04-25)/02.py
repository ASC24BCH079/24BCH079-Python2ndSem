def print_pattern(n):
    for i in range(n-2, 0, -1):
        if i==n//2:
            gap=' '*(n-i-1)
            print('*'*i+gap+"   - for n = "+str(n))
        else:
            print('*'*i)

lines=input("Enter number of lines: ")
if lines.isdigit():
    print_pattern(int(lines))
else:
    print("Not a valid number")
