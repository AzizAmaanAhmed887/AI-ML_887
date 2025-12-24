class Laptop:
    storage_type = "SSD"  # class variable

    @classmethod
    def change_storage_type(cls, storage_type):
        cls.storage_type = storage_type