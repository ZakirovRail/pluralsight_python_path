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


class SlotsInspectionMixin:
    def has_slots(self):
        return hasattr(self, "__slots__")


class Developer(SlotsInspectionMixin, Employee):
    __slots__ = ("name", "age", "salary", "framework", )

    def __init__(self, name, age, salary, framework):
        super().__init__(name, age, salary)
        self.framework = framework

    def increase_salary(self, percent, bonus=0):
        super().increase_salary(percent)
        # Employee.increase_salary(self, percent)
        self.salary += bonus


employee2 = Developer("Ji-Soo", 38, 1200, "Flask")
print(employee2.has_slots())
