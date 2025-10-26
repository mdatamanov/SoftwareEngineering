filename = input("Введите имя файла: ")
search_word = input("Какое слово ищем: ")

try:
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
        count = content.lower().count(search_word.lower())
        print(f"Слово '{search_word}' найдено {count} раз")
except FileNotFoundError:
    print("Файл не найден")