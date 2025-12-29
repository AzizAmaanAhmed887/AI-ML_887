class Person:
    def __init__(self, name):
        self.name = name


class Student(Person):
    def __init__(self, name, roll):
        super().__init__(name) # super() to access parent class
        self.roll = roll

s1 = Student("Amaan", 65)
print(s1.name, s1.roll)

print("-------------------------------------")

# single level inheritance
class Employee:
    start_time = "10am"
    end_time = "5pm"


class Teacher(Employee):
    def __init__(self, subject):
        self.subject = subject


t1 = Teacher("Maths")
t2 = Teacher("Physics")

print(t1.subject, t1.start_time, t1.end_time)
print("-------------------------------------")
print(t2.subject, t2.start_time, t2.end_time)
