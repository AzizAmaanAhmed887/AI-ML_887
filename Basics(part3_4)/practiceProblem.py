class Product:
    count = 0
    def __init__(self, name, price):
        self.name = name
        self.price = price
        Product.count+=1

    def getInfo(self):
        print(f"'{self.name}' is of price 'Rs.{self.price}'")

    def getCount(self):
        print(f"Total product count = {self.count}")


p1 = Product("Phone", 10_000)
p2 = Product("Laptop", 50_000)
p3 = Product("Pen", 10)

Product.getCount(p1)
