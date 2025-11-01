from Sam_work.Sam_8.sam2_8 import Smartphone

# Наследование - создаем класс игрового смартфона
class GamingSmartphone(Smartphone):
    def __init__(self, brand, model, storage, cooling_system, refresh_rate):
        # Вызываем конструктор родительского класса
        super().__init__(brand, model, storage)
        # Добавляем новые атрибуты
        self.cooling_system = cooling_system
        self.refresh_rate = refresh_rate

    def play_game(self, game_name):
        print(f"Запускаем игру '{game_name}' на {self.brand} {self.model}")
        print(f"Частота обновления: {self.refresh_rate} Гц")

    # Переопределяем метод display_info
    def display_info(self):
        super().display_info()  # вызываем метод родителя
        print(f"Система охлаждения: {self.cooling_system}")
        print(f"Частота обновления экрана: {self.refresh_rate} Гц")


# Создаем обычный смартфон
phone1 = Smartphone("Samsung", "Galaxy S21", 128)
phone1.display_info()
print()

# Создаем игровой смартфон
gaming_phone = GamingSmartphone("ASUS", "ROG Phone 6", 256, "активная", 165)
gaming_phone.display_info()
gaming_phone.play_game("Genshin Impact")