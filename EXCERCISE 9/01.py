import csv
def make_csv_file():
    fields = ['Roll', 'Name', 'Branch']
    students = [
        [1, 'Amit', 'CSE'],
        [2, 'Sneha', 'ECE'],
        [3, 'Ravi', 'CHEM']
    ]
    with open('student_data.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(fields)
        for s in students:
            writer.writerow(s)
make_csv_file()
