def read_file_with_validation(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            content = file.read()

            if not content.strip():  # Проверяем, не пустой ли файл
                raise ValueError("файл пустой")

            return content

    except FileNotFoundError:
        return "Файл не найден"
    except ValueError as e:
        return str(e)
    except Exception as e:
        return f"Произошла ошибка: {e}"


# Тестирование
if __name__ == "__main__":
    # Создаем тестовые файлы
    with open('empty_file.txt', 'w', encoding='utf-8') as f:
        pass  # Создаем пустой файл

    with open('non_empty_file.txt', 'w', encoding='utf-8') as f:
        f.write("Это файл с информацией!\n")
        f.write("Здесь есть несколько строк текста.\n")
        f.write("Данные для обработки.")

    print("Тест с пустым файлом:")
    result1 = read_file_with_validation('empty_file.txt')
    print(result1)

    print("\nТест с непустым файлом:")
    result2 = read_file_with_validation('non_empty_file.txt')
    print(result2)

    print("\nТест с несуществующим файлом:")
    result3 = read_file_with_validation('nonexistent_file.txt')
    print(result3)