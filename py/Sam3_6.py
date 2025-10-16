# Получаем строку от пользователя
numbers_string = input("Введите последовательность чисел (минимум 15 символов): ")

# Проверяем длину строки
if len(numbers_string) < 15:
    print("Ошибка: строка должна содержать минимум 15 символов!")
else:
    # Создаем словарь для подсчета чисел
    count_dict = {}

    # Перебираем каждый символ в строке
    for char in numbers_string:
        # Преобразуем символ в число
        num = int(char)

        # Увеличиваем счетчик для этого числа
        if num in count_dict:
            count_dict[num] += 1
        else:
            count_dict[num] = 1

    # Выводим результат
    print("Результат подсчета:")
    for number, count in sorted(count_dict.items()):
        print(f"Цифра {number}: {count} раз(а)")

    # Определяем победителя (цифра с максимальным количеством)
    max_count = max(count_dict.values())
    winning_numbers = [num for num, count in count_dict.items() if count == max_count]

    print(f"\nПобедитель(и): цифра {winning_numbers} - набрана {max_count} раз(а)")