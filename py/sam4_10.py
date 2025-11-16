import time


class FormatOutputDecorator:
    def __init__(self, border_char="*", width=50):
        self.border_char = border_char
        self.width = width

    def __call__(self, func):
        def wrapper(*args, **kwargs):
            # Верхняя граница
            print(self.border_char * self.width)

            # Заголовок с именем функции
            print(f"{self.border_char} Выполняется функция: {func.__name__} {self.border_char}")
            print(self.border_char * self.width)

            # Выполнение функции
            start_time = time.time()
            result = func(*args, **kwargs)
            end_time = time.time()

            # Вывод результата
            print(f"{self.border_char} Результат: {result}")

            # Время выполнения
            execution_time = end_time - start_time
            print(f"{self.border_char} Время выполнения: {execution_time:.6f} сек")

            # Нижняя граница
            print(self.border_char * self.width)
            print()  # Пустая строка для разделения

            return result

        return wrapper


# Создаем экземпляр декоратора
format_output = FormatOutputDecorator(border_char="═", width=60)


# Функции, использующие декоратор
@format_output
def calculate_factorial(n):
    if n < 0:
        return "Факториал отрицательного числа не определен"

    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


@format_output
def generate_fibonacci_sequence(count):
    if count <= 0:
        return []

    sequence = [0, 1]
    if count == 1:
        return [0]
    elif count == 2:
        return sequence

    for i in range(2, count):
        sequence.append(sequence[i - 1] + sequence[i - 2])

    return sequence


# Демонстрация работы
if __name__ == "__main__":
    print("ДЕМОНСТРАЦИЯ ПОЛЬЗОВАТЕЛЬСКОГО ДЕКОРАТОРА")
    print()

    # Тестируем первую функцию
    calculate_factorial(5)

    # Тестируем вторую функцию
    generate_fibonacci_sequence(10)

    # Еще тесты
    calculate_factorial(7)
    generate_fibonacci_sequence(5)