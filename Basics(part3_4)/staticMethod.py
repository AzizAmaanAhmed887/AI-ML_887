class Laptop:
    @staticmethod
    def is_valid_ram(ram):
        return ram in ["4gb", "8gb", "16gb", "32gb"]


print(Laptop.is_valid_ram("4gb"), Laptop.is_valid_ram("3gb"))  # true, false
