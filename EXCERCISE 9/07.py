import pickle

class Employee:
    def __init__(self, code, name, doj, salary):
        self.code = code
        self.name = name
        self.doj = doj
        self.salary = salary

def save_and_load_employee():
    emp = Employee(101, 'Keshav Sharma', '2025-04-04', 55000)

    with open('empdata.pkl', 'wb') as f:
        pickle.dump(emp, f)
    print("Employee data saved to file.")

    with open('empdata.pkl', 'rb') as f:
        loaded_emp = pickle.load(f)

    print("\nEmployee data loaded from file:")
    print("Code:", loaded_emp.code)
    print("Name:", loaded_emp.name)
    print("Date of Joining:", loaded_emp.doj)
    print("Salary:", loaded_emp.salary)

if __name__ == "__main__":
    save_and_load_employee()
