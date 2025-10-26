
with open('forbidden.txt', 'w', encoding='utf-8') as f:
    f.write("hello email python the exam wor is")

with open('forbidden.txt', 'r', encoding='utf-8') as f:
    bad_words = f.read().split()

text = "Hello, world! Python IS the programming language of thE future. My EMAIL is... PYTHON is awesome!!!!"

result = text
for word in bad_words:
    start = 0
    while True:
        found_index = result.lower().find(word, start)
        if found_index == -1:
            break

        result = result[:found_index] + '*' * len(word) + result[found_index + len(word):]
        start = found_index + len(word)

print("Исходный текст:")
print(text)
print("\nРезультат:")
print(result)