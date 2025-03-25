import math
xc, yc = map(float,input("Enter the coordinates of the center(x y):").split())
r = float(input("Enter the radius of the circle:"))
x, y = map(float,input("Enter the coordinates of the point(x y):").split())
d = math.sqrt(pow(x-xc,2) + pow(y-yc,2))
if d<r:
    print("The point is inside the circle.")
elif d==r:
    print("The point is on the circle.")
else:
    print("The point is outside the circle.")
