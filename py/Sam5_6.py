def calculate_average_grades(students_data):
    result = {}

    for student in students_data:
        name = student[0]
        grades = student[1]

        # Рассчитываем средний балл
        if grades:  # проверяем, что список оценок не пустой
            average = sum(grades) / len(grades)
        else:
            average = 0  # если нет оценок

        result[name] = round(average, 2)  # округляем до 2 знаков

    return result


# Тест 1: Обычный случай
print("Тест 1: Обычный случай")
students1 = (
    ("Анна", [4, 5, 5, 4, 3]),
    ("Иван", [3, 4, 5, 3, 4]),
    ("Мария", [5, 5, 5, 5, 5])
)
result1 = calculate_average_grades(students1)
print(f"Результат: {result1}")
print("Ожидаем: Анна - 4.2, Иван - 3.8, Мария - 5.0")
print()

# Тест 2: Студент без оценок
print("Тест 2: Студент без оценок")
students2 = (
    ("Петр", [4, 3, 5]),
    ("Ольга", []),  # нет оценок
    ("Сергей", [2, 3, 2, 4])
)
result2 = calculate_average_grades(students2)
print(f"Результат: {result2}")
print("Ожидаем: Петр - 4.0, Ольга - 0.0, Сергей - 2.75")
print()

# Тест 3: Один студент
print("Тест 3: Один студент")
students3 = (
    ("Алексей", [5, 4, 5, 3, 5, 4]),
)
result3 = calculate_average_grades(students3)
print(f"Результат: {result3}")
print("Ожидаем: Алексей - 4.33")
print()

# Дополнительный тест: Все студенты без оценок
print("Дополнительный тест: Все без оценок")
students4 = (
    ("Дмитрий", []),
    ("Елена", [])
)
result4 = calculate_average_grades(students4)
print(f"Результат: {result4}")
print("Ожидаем: Дмитрий - 0.0, Елена - 0.0")