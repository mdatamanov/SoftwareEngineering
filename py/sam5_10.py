# Создаем собственное исключение
class MyCustomError(Exception):
    pass


# Первая функция, которая использует наше исключение
def check_positive_number(number):
    if number < 0:
        raise MyCustomError(f"Число {number} отрицательное! Должно быть положительным.")
    return f"Число {number} положительное - всё OK!"


# Вторая функция, которая тоже использует наше исключение
def check_even_number(number):
    if number % 2 != 0:
        raise MyCustomError(f"Число {number} нечетное! Должно быть четным.")
    return f"Число {number} четное - всё OK!"


# Демонстрация работы
if __name__ == "__main__":
    print("=== ДЕМОНСТРАЦИЯ СОБСТВЕННОГО ИСКЛЮЧЕНИЯ ===\n")

    # Тестовые данные
    test_numbers = [5, -3, 10, 7, -8, 4]

    for number in test_numbers:
        print(f"Проверяем число: {number}")

        # Тестируем первую функцию
        try:
            result1 = check_positive_number(number)
            print(f"Проверка на положительность: {result1}")
        except MyCustomError as e:
            print(f"Ошибка в проверке на положительность: {e}")

        # Тестируем вторую функцию
        try:
            result2 = check_even_number(number)
            print(f"Проверка на четность: {result2}")
        except MyCustomError as e:
            print(f"Ошибка в проверке на четность: {e}")

        print("-" * 50)

    print("\n=== КОНЕЦ ДЕМОНСТРАЦИИ ===")