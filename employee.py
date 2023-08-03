class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

# method repr represent information on the screen
    def __repr__(self):
        return'({},{},${})'.format(self.name, self.age, self.salary)


# create three objects
e1 = Employee('Ilyes', 25, 45000)
e2 = Employee('Hafid', 28, 50000)
e3 = Employee('Sara', 24, 55000)

# put e1, e2, e3 in a list
employer = [e1, e2, e3]


def e_sort(emp):
    return emp.salary


sorted_employees = sorted(employer, key=lambda e: e.name, reverse=True)
# sorted_employees = sorted(employer, key=e_sort, reverse=True)
print(sorted_employees)
