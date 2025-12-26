class bankAccount:
    def __init__(self, name, amount):
        self.name = name
        self.amount = amount + 30
        print(f"Name: {self.name}, Amount: Rs.{self.amount}")


# bankAccount("Rahul Kumar", 10_000)

class Student:
    def __init__(self):
        self.__marks = 0

    def set_marks(self, nm):
        self.__marks = nm

    def get_marks(self):
        return f"New marks = {self.__marks}"

s = Student()
s.set_marks(98)
print(s.get_marks())