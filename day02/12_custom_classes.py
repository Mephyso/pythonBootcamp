
class Employee:
    company = "Google Inc."

    def __init__(self, name: str = "Adam", job: str = "Work", ident: str = "E0000", age: int = 18, salary: int = 12000):
        self.name = name
        self.job = job
        self.ident = ident
        self.age = age
        self.salary = salary

    def work(self):
        print(f"{self.name} is working very hard.")

    def __str__(self):
        return f"{type(self).__name__} {self.__dict__}"     # easiest way to access all information of object


"""
    def __str__(self):
        return f"{self.name} {self.job} {self.ident} {self.age} {self.salary} {self.company}"
"""

E1 = Employee("John Wick", "Worker", "E0001", 25, 24000)
E1.work()
print(E1)

E2 = Employee("Christopher Nolan")
E2.work()
E2.job = "Manager"
E2.ident = "E0002"
print(E2)
