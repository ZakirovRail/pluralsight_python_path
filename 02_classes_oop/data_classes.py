# class Project:
#     def __init__(self, name, payment, client):
#         self.name = name
#         self.payment = payment
#         self.client = client
#
#     def __repr__(self):
#         return f"Project(name={repr(self.name)}, payment={repr(self.payment)}, client={repr(self.client)})"
#
#
# class Employee:
#     def __init__(self, name, age, salary, project):
#         self.name = name
#         self.age = age
#         self.salary = salary
#         self.project = project
#
#
# p = Project("Django app", 20000, "Globomantics")
# e = Employee("Ji-Soo", 38, 1200, p)
# print(e.project)



# =====================================================================================================================

from dataclasses import dataclass


@dataclass(slots=True)
class Project:
    name: str
    payment: int
    client: str

    def notify_client(self):
        print(f"Notifying about the progress of the {self.name}")


class Employee:
    def __init__(self, name, age, salary, project):
        self.name = name
        self.age = age
        self.salary = salary
        self.project = project


p = Project("Django app", 20000, "Globomantics")
e = Employee("Ji-Soo", 38, 1200, p)
print(e.project)









