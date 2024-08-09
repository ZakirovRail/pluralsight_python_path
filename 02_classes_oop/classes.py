# class Employee:
#     def __init__(self):
#         self.__dict__["name"] = "Ji-Soo"
#         self.__dict__["age"] = 38
#         self.__dict__["position"] = "developer"
#         self.__dict__["salary"] = 1200
#
#
# e = Employee()
# print(e.__dict__)

# =====================================================================================================================

# class Employee:
#     def __init__(self, name, age, position, salary):
#         self.name = name
#         self.age = age
#         self.position = position
#         self.salary = salary
#
#
# employee1 = Employee("Ji-Soo", 38, "developer", 1200)
# employee2 = Employee("Lauren", 44, "tester", 1000)
#
# print(employee1.name)
# print(employee2.name)


# =====================================================================================================================

class Employee:
    def __init__(self, name, age, position, salary):
        self.name = name
        self.age = age
        self.position = position
        self.salary = salary

    def increase_salary(self, percent):
        self.salary += self.salary * (percent/100)

    def __str__(self):
        return f"{self.name} is {self.age} years old. Employee is a {self.position} with a salary of ${self.salary} "

    def __repr__(self):
        return (f"Employee({repr(self.name)}, {repr(self.age)}, {repr(self.position)}, {repr(self.salary)})")


employee1 = Employee("Ji-Soo", 38, "developer", 1200)
employee2 = Employee("Lauren", 44, "tester", 1000)

print(employee1.name)
print(employee2.name)
Employee.increase_salary(employee2, 20)

employee2.increase_salary(20)
print(employee2.name)
print(employee2.salary)
print("============")
print(employee1)
print(repr(employee1))
print(eval(repr(employee1)))
