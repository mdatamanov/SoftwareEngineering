def fib(n):
    a, b = 1, 1
    count = 0
    while count < n:
        yield a
        a, b = b, a + b
        count += 1
def save_fib_to_file(n, filename="fib.txt"):
    with open(filename, 'w', encoding='utf-8') as file:
        fib_gen = fib(n)

        for number in fib_gen:
            file.write(f"{number}\n")

    print(f"Все {n} чисел Фибоначчи сохранены в файл '{filename}'")
def main():
    save_fib_to_file(200)
    with open("fib.txt", 'r', encoding='utf-8') as file:
        lines = file.readlines()
        print(f"Всего чисел в файле: {len(lines)}")
        print(f"Первые 5 чисел: {[line.strip() for line in lines[:5]]}")
        print(f"Последнее (200-е) число: {lines[-1].strip()}")
if __name__ == "__main__":
    main()