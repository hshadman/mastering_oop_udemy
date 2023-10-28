class Employee:
    def __init__(self,age,Name,annual_salary):
        self.age=age
        self.name=Name
        self.salary=annual_salary
    def get_raise(self,bonus):
        self.salary += bonus
    def get_name(self):
        return self.name
    def inc_age(self):
        self.age += 1
    def get_age(self):
        return self.age
    def get_salary(self):
        return self.salary
e1 = Employee("Alice",20,10000)
print(e1.get_name())
print(e1.get_age())
print(e1.get_salary())
e2=Employee("Bob",30,20000)
