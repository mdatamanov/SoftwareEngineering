# Добавить расход
def add_expense():
    with open('expenses.txt', 'a', encoding='utf-8') as f:
        item = input("Что купили: ")
        price = input("Сколько стоит: ")
        f.write(f"{item} - {price} руб\n")
    print("Расход добавлен!")


# Показать расходы
def show_expenses():
    try:
        with open('expenses.txt', 'r', encoding='utf-8') as f:
            print("Ваши расходы:")
            print(f.read())
    except FileNotFoundError:
        print("Расходов пока нет")


# Главное меню
while True:
    print("\n1 - Добавить расход")
    print("2 - Показать расходы")
    print("3 - Выход")
    choice = input("Выберите: ")

    if choice == '1':
        add_expense()
    elif choice == '2':
        show_expenses()
    elif choice == '3':
        break