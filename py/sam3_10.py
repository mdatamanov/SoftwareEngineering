def add_two():
    try:
        user_input = input("Введите число для сложения с 2: ")
        number = float(user_input)  # Пробуем преобразовать в число

        result = 2 + number
        print(f"Результат: 2 + {number} = {result}")
        return result

    except ValueError:
        print("Неподходящий тип данных. Ожидалось число.")
        return None


# Тестирование функции
if __name__ == "__main__":
    print("=== Тест 1: Корректный ввод ===")
    add_two()

    print("\n=== Тест 2: Ввод строки ===")
    add_two()

    print("\n=== Тест 3: Ввод дробного числа ===")
    add_two()

    print("\n=== Тест 4: Ввод с пробелами ===")
    add_two()