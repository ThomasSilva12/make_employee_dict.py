### Thomas Silva
### ENGR 103 Assignment 8c.
### Nov 22, 2023.


class Employee:
    def __init__(self, name, id_number, salary, email_address):
        self._name = name
        self._id_number = id_number
        self._salary = salary
        self._email_address = email_address

    def get_name(self):
        return self._name

    def get_id_number(self):
        return self._id_number

    def get_salary(self):
        return self._salary

    def get_email_address(self):
        return self._email_address


def make_employee_dict(names, id_numbers, salaries, email_addresses):
    employee_dict = {}

    for name, id_number, salary, email_address in zip(names, id_numbers, salaries, email_addresses):
        employee = Employee(name, id_number, salary, email_address)

        employee_dict[id_number] = employee

    return employee_dict

names = ["Alice", "Bob", "Charlie"]
id_numbers = [101, 102, 103]
salaries = [50000, 60000, 70000]
email_addresses = ["alice@gmail.com", "bob@gmail.com", "charlie@gmail.com"]

employee_dict = make_employee_dict(names, id_numbers, salaries, email_addresses)

for id_number, employee in employee_dict.items():
    print(f"Employee ID: {id_number}")
    print(f"Name: {employee.get_name()}")
    print(f"Salary: {employee.get_salary()}")
    print(f"Email Address: {employee.get_email_address()}")
    print()
