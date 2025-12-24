class Student:
    def __init__(self, name, college, cgpa):
        self.name = name
        self.college = college
        self.cgpa = cgpa

    def get_cgpa(self):
        return self.cgpa

s1 = Student("Amaan", "SRIST", 6.4)
s2 = Student("Azaj", "SRIST", 7.4)
s3 = Student("Aryan", "SRIST", 8.4)
print(s1.get_cgpa())
print(s2.get_cgpa())
print(s3.get_cgpa())