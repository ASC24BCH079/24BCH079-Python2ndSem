nw = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine",  "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
n = int(input("Enter a number between 0 and 19:"))
if 0<=n<=19:
    print("The entered number in words is:", nw[n])
else:
    print("Please enter a number between 0 and 19.")

