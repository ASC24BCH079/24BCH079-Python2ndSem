p = float(input("Enter marks in Physics: "))
c = float(input("Enter marks in Chemistry: "))
b = float(input("Enter marks in Biology: "))
average = (p+c+b)/3
if average >= 80:
    grade = "Distinction"
elif average >= 60:
    grade = "First Division"
elif average >= 45:
    grade = "Second Division"
elif average >= 40:
    grade = "Pass"
else:
    grade = "Promotion not granted"
print(f"Marks Percentage: {round(average,2)}%")
print(f"Grade Obtained: {grade}")