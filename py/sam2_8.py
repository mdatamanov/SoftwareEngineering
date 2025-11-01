class Smartphone:
    def __init__(self, brand, model, storage):
        self.brand = brand
        self.model = model
        self.storage = storage  # объем памяти в ГБ

    def display_info(self):
        print(f"Смартфон: {self.brand} {self.model}")
        print(f"Память: {self.storage} ГБ")

phone1 = Smartphone("Samsung", "Galaxy S21", 128)
phone1.display_info()