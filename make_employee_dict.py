# Author: Matthew Armstrong
# Date: 7/25/21
# Description: returns a dictionary holding employee data
class Employee:
    """Represents a class which holds the data of employees"""
    # init method to set private fields for employee details
    def __init__(self, name, ID_number, salary, email_address):
        """creates a class which holds the data of employees"""
        self._name = name
        self._ID_number = ID_number
        self._salary = salary
        self._email_address = email_address

    def get_name(self):
        """returns the name"""
        return self._name

    def get_ID_number(self):
        """returns the ID"""
        return self._ID_number

    def get_salary(self):
        """returns the salary"""
        return self._salary

    def get_email_address(self):
        """returns the email"""
        return self._email_address


def make_employee_dict(names, ids, salaries, emails):
    """returns the employee dictionary"""
    emp_dict = {}
    list_len = len(ids)
    for i in range(list_len):
        name = names[i]
        id_num = ids[i]
        salary = salaries[i]
        email = emails[i]
        emp_dict[id_num] = Employee(name, id_num, salary, email)
    return emp_dict
