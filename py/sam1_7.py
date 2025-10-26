from collections import Counter

with open('article.txt', 'r', encoding='utf-8') as f:
    text = f.read()

words = text.lower().replace(',', '').replace('.', '').replace('!', '').replace('?', '').split()

real_words = [word for word in words if len(word) > 2]

word_count = len(real_words)

if real_words:
    most_common = Counter(real_words).most_common(1)[0]
    print(f"Количество слов (без предлогов): {word_count}")
    print(f"Самое частое слово: '{most_common[0]}' ({most_common[1]} раз)")
else:
    print("Нет подходящих слов")