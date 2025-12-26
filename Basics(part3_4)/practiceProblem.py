from itertools import product


class Product:
    count = 0

    def __init__(self, name, price):
        self.name = name
        self.price = price
        Product.count += 1

    def getInfo(self):
        print(f"'{self.name}' is of price 'Rs.{self.price}'")

    @classmethod
    def getCount(cls):
        print(f"Total product count = {cls.count}")

    @staticmethod
    def getDiscount(price, discount):
        return f"Discounted price = Rs.{price - (price * discount / 100)}"

# p1 = Product("Phone", 10_000)
# p2 = Product("Laptop", 50_000)
# p3 = Product("Pen", 10)

p4 = Product.getDiscount(10_000, 10)

print(p4)