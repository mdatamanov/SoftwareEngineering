class Smartphone:
    def __init__(self, brand, model, storage, price):
        self.brand = brand
        self.model = model
        self.storage = storage
        self.__price = price  # приватный атрибут
        self._discount = 0  # защищенный атрибут

    # Геттер для получения цены
    def get_price(self):
        return self.__price

    # Сеттер для установки цены
    def set_price(self, new_price):
        if new_price > 0:
            self.__price = new_price
            print(f"Цена изменена на {new_price} руб.")
        else:
            print("Цена должна быть положительной!")

    # Метод для установки скидки
    def set_discount(self, discount_percent):
        if 0 <= discount_percent <= 50:
            self._discount = discount_percent
            print(f"Скидка установлена: {discount_percent}%")
        else:
            print("Скидка должна быть от 0% до 50%")

    # Метод для расчета цены со скидкой
    def get_final_price(self):
        return self.__price * (1 - self._discount / 100)

    def display_info(self):
        print(f"Смартфон: {self.brand} {self.model}")
        print(f"Память: {self.storage} ГБ")
        print(f"Цена: {self.__price} руб.")
        print(f"Скидка: {self._discount}%")
        print(f"Итоговая цена: {self.get_final_price():.2f} руб.")


phone = Smartphone("Xiaomi", "Redmi Note 10", 64, 15999)
phone.display_info()
print()

# Работа с инкапсулированными данными
phone.set_discount(15)
phone.display_info()
print()

phone.set_price(14999)
phone.display_info()
print()

# Попытка прямого доступа к приватному атрибуту (не сработает)
# print(phone.__price)  # Вызовет ошибку!

# Корректный доступ через геттер
print(f"Текущая цена через геттер: {phone.get_price()} руб.")