def get_office_sequence(tuple_data, employee_id):
    # Если элемента нет в кортеже
    if employee_id not in tuple_data:
        return ()

    # Находим индекс первого вхождения
    first_index = tuple_data.index(employee_id)

    # Находим индекс второго вхождения
    # Ищем начиная с позиции после первого вхождения
    try:
        second_index = tuple_data.index(employee_id, first_index + 1)
        # Возвращаем срез от первого до второго вхождения включительно
        return tuple_data[first_index:second_index + 1]
    except ValueError:
        # Если второго вхождения нет - возвращаем от первого до конца
        return tuple_data[first_index:]


# Тестирование на примерах из задания
test_cases = [
    ((1, 2, 3), 8),
    ((1, 8, 3, 4, 8, 8, 9, 2), 8),
    ((1, 2, 8, 5, 1, 2, 9), 8)
]

print("Результаты:")
for i, (tpl, elem) in enumerate(test_cases, 1):
    result = get_office_sequence(tpl, elem)
    print(f"Тест {i}: {result}")