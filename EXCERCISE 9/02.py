import pandas as pd
def read_excel_and_dict():
    data = pd.read_excel('marksheet.xlsx')
    info = {}
    for i, row in data.iterrows():
        total = row['sub1'] + row['sub2'] + row['sub3']
        info[row['rollno']] = {
            'name': row['name'],
            'marks': [row['sub1'], row['sub2'], row['sub3']],
            'total': total
        }
    for r in info:
        print('Roll:', r)
        print(info[r])
        print()
read_excel_and_dict()

