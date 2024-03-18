
class Employee:
    minimum_wage = 1000

    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def increase_salary(self, percent):
        self.salary += self.salary * (percent/100)

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, salary):
        if salary < Employee.minimum_wage:
            raise ValueError(f'Minimum wage is ${Employee.minimum_wage}')
        self._salary = salary

# print(Employee.__dict__)
# for attribute, value in Employee.__dict__.items():
#     print(f"{attribute}:{value}")


e = Employee("Ji-Soo", 38, 1000)
print(e.minimum_wage)