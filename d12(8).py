# Tuples + Dictionaries + OOP

class Employee:
    def __init__(self, emp_id, name, details):
        self.emp_id = emp_id
        self.name = name
        self.details = details   # tuple (department, salary)

    def show_details(self):
        print("\nEmployee ID:", self.emp_id)
        print("Name:", self.name)
        print("Department:", self.details[0])
        print("Salary:", self.details[1])
        print("----------------------")


employees = {}

try:
    # Adding 3 employees using user input
    for i in range(3):
        print("\nEnter details of Employee", i+1)

        emp_id = int(input("Enter Employee ID: "))
        name = input("Enter Employee Name: ")
        department = input("Enter Department: ")
        salary = float(input("Enter Salary: "))

        details = (department, salary)

        employee = Employee(emp_id, name, details)

        employees[emp_id] = employee

    # Display all employees
    print("\n--- Employee Details ---")

    for emp_id, employee in employees.items():
        employee.show_details()

except ValueError:
    print("Invalid input! Enter correct values.")

except Exception as e:
    print("Error:", e)