class Smartphone:
    def __init__(self, brand, model, storage):
        self.brand = brand
        self.model = model
        self.storage = storage

    def make_call(self, number):
        return f"{self.brand} {self.model} звонит на номер {number}"

    def display_info(self):
        return f"Смартфон: {self.brand} {self.model}, Память: {self.storage} ГБ"


# Другой класс с таким же методом
class Tablet:
    def __init__(self, brand, model, screen_size):
        self.brand = brand
        self.model = model
        self.screen_size = screen_size

    def make_call(self, number):
        return f"Планшет {self.brand} {self.model} звонит на номер {number}"

    def display_info(self):
        return f"Планшет: {self.brand} {self.model}, Экран: {self.screen_size}\""


# Еще один класс с таким же методом
class SmartWatch:
    def __init__(self, brand, model, battery_life):
        self.brand = brand
        self.model = model
        self.battery_life = battery_life

    def make_call(self, number):
        return f"Смарт-часы {self.brand} {self.model} звонят на номер {number}"

    def display_info(self):
        return f"Смарт-часы: {self.brand} {self.model}, Батарея: {self.battery_life} дней"


# Функция, демонстрирующая полиморфизм
def use_device(device, number):
    """Эта функция работает с любым устройством, у которого есть методы make_call и display_info"""
    print(device.display_info())
    print(device.make_call(number))
    print("---")


# Создаем разные устройства
devices = [
    Smartphone("Samsung", "Galaxy S21", 128),
    Tablet("Apple", "iPad Air", 10.9),
    SmartWatch("Xiaomi", "Mi Band 7", 14),
    Smartphone("Apple", "iPhone 14", 256)
]

# Демонстрация полиморфизма
print("Демонстрация полиморфизма:")
for device in devices:
    use_device(device, "+7-999-123-45-67")

# Еще один пример полиморфизма
print("\nМассив разных устройств:")
for device in devices:
    # Полиморфный вызов метода - один интерфейс, разное поведение
    call_result = device.make_call("+7-495-111-22-33")
    print(call_result)