def fix_grades(grades):
    fixed_grades = grades.copy()
    fixed_grades = [grade for grade in fixed_grades if grade != 2]
    fixed_grades = [4 if grade == 3 else grade for grade in fixed_grades]
    return fixed_grades

grades_list_1 = [2, 3, 4, 5, 3, 4, 5, 2, 2, 5, 3, 4, 3, 5, 4]
grades_list_2 = [4, 2, 3, 5, 3, 5, 4, 2, 2, 5, 4, 3, 5, 3, 4]
grades_list_3 = [5, 4, 3, 3, 4, 3, 3, 5, 5, 3, 3, 3, 3, 4, 4]

print("1-й список оценок:")
print(f"Исходный: {grades_list_1}")
fixed_1 = fix_grades(grades_list_1)
print(f"Исправленный: {fixed_1}")
print(f"Количество оценок: было {len(grades_list_1)}, стало {len(fixed_1)}")

print("\n2-й список оценок:")
print(f"Исходный: {grades_list_2}")
fixed_2 = fix_grades(grades_list_2)
print(f"Исправленный: {fixed_2}")
print(f"Количество оценок: было {len(grades_list_2)}, стало {len(fixed_2)}")

print("\n3-й список оценок:")
print(f"Исходный: {grades_list_3}")
fixed_3 = fix_grades(grades_list_3)
print(f"Исправленный: {fixed_3}")
print(f"Количество оценок: было {len(grades_list_3)}, стало {len(fixed_3)}")
