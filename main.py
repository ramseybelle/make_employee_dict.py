class Employee:
    def __init__(self, name, ID, salary, email_address):
        self.name = name
        self.ID = ID
        self.salary = salary
        self.email_address = email_address


def make_employee_dict(emp_names, emp_ids, emp_sals, emp_emails):
    dict_final = {}
    for i in range(len(emp_ids)):
        dict_final[emp_ids[i]] = Employee(emp_names[i], emp_ids[i], emp_sals[i], emp_emails[i])

    return dict_final


emp_names = ["Jean", "Kat", "Pomona"]
emp_ids = ["100", "101", "102"]
emp_sals = [30, 35, 28]
emp_emails = ["Jean@aol.com", "Kat@aol.com", "Pomona@aol.com"]
result = make_employee_dict(emp_names, emp_ids, emp_sals, emp_emails)
print(result)
