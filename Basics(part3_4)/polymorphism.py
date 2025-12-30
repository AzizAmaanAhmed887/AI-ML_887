class Employee:
    def getCity(self):
        print("City = Jabalpur")


class Teacher(Employee):
    def getCity(self):
        print("City = Bhopal")

t1 = Teacher()
t1.getCity() # City = Bhopal