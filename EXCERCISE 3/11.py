print("The entries should be separated by space in the format {(x y)}")
x1,y1 = map(int, input("Enter coordinates of point 1:").split())
x2,y2 = map(int, input("Enter coordinates of point 2:").split())
x3,y3 = map(int, input("Enter coordinates of point 3:").split())
if (x2-x1)*(y3-y1) == (y2-y1)*(x3-x1):
    print("The points are collinear.")
else:
    print("The points are not collinear.")