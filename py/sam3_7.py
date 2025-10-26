# Создаем файл с текстом
with open('input.txt', 'w', encoding='utf-8') as f:
    f.write("""Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.""")

# Анализируем
with open('input.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()

letters = sum(len([c for c in line if c.isalpha()]) for line in lines)
words = sum(len(line.split()) for line in lines)
line_count = len(lines)

print(f"Input file contains:")
print(f"{letters} letters")
print(f"{words} words")
print(f"{line_count} lines")