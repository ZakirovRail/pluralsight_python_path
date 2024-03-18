# class Developer:
#     __slots__ = ("name", "age", "salary", "framework")
#
#     def __init__(self, name, age, salary, framework):
#         self.name = name
#         self.age = age
#         self.salary = salary
#         self.framework = framework
#
#
# employee1 = Developer("Ji-Soo", 38, 1200, "Flask")
#
# print(employee1.__slots__)
# =====================================================================================================================

class Employee:
    __slots__ = ("name", "age", "salary")

    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def increase_salary(self, percent):
        self.salary += self.salary * (percent/100)

    def __repr__(self):
        return f"This is instance of {self.__class__} class with attributes:" \
               f"{self.name}, {self.age}, {self.salary}"


class Tester(Employee):

    def run_tests(self):
        print(f"Testing is started by {self.name}...")
        print("Tests are done.")


class Developer(Employee):
    __slots__ = ("name", "age", "salary", "framework", )

    def __init__(self, name, age, salary, framework):
        super().__init__(name, age, salary)
        self.framework = framework

    def increase_salary(self, percent, bonus=0):
        super().increase_salary(percent)
        # Employee.increase_salary(self, percent)
        self.salary += bonus


employee1 = Tester("Lauren", 44, 1000)
employee2 = Developer("Ji-Soo", 38, 1200, "Flask")
print(employee2.__slots__)
print(employee1.__repr__())
print(employee2.__repr__())
# employee1.increase_salary(20)
# employee2.increase_salary(20, 30)
# print(employee1.salary)
# print(employee2.salary)

