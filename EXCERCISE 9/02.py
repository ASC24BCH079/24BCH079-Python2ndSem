import pandas as pd
import os

if os.path.exists('students_data.xlsx'):
    df = pd.read_excel('students_data.xlsx')
else:
    print("'students_data.xlsx' file not found.")
    df = pd.DataFrame()

students_list = df.to_dict(orient='records') if not df.empty else []

for student in students_list:
    m1 = student.get('marks_subject1', 0)
    m2 = student.get('marks_subject2', 0)
    m3 = student.get('marks_subject3', 0)
    student['total'] = m1 + m2 + m3

print(students_list)
