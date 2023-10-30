class Student:
    def __init__(self, first_name,last_name):
        self.first_name = first_name
        self.last_name = last_name
    @classmethod
    def from_fullname(cls,full_name):
        first, last = full_name.split(" ")
        cls(first,last) #equivalent to Student(first,last) cls is actually class
        return cls(first, last)
    @classmethod
    def from_json(cls, json):
        #process input
        return cls(first, last)
s1 = Student("Alex", "Baldwin")
print(s1.first_name,s1.last_name)
#python allows method overwriting, not overloading, unlike C++

s2 = Student.from_fullname ("Tom Hanks")
print(type(s2))
print(s2.first_name)
print(s2.last_name)