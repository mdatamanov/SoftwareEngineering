one = [12, 25, 3, 48, 71]
two = [5, 18, 40, 62, 98]
three = [4, 21, 37, 56, 84]

print("Исходные списки:")
print(f"one = {one}")
print(f"two = {two}")
print(f"three = {three}")
min_a = min(one)
min_b = min(two)
min_c = min(three)
max_a = max(one)
max_b = max(two)
max_c = max(three)

print(f"\nМинимальные элементы: {min_a}, {min_b}, {min_c}")
print(f"Максимальные элементы: {max_a}, {max_b}, {max_c}")

# Функция для проверки существования треугольника и вычисления площади
def calculate_triangle_area(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        p = (a + b + c) / 2
        area = (p * (p - a) * (p - b) * (p - c)) ** 0.5
        return area
    else:
        return None

# Вычисляем площадь треугольника из минимальных элементов
area_min = calculate_triangle_area(min_a, min_b, min_c)

# Вычисляем площадь треугольника из максимальных элементов
area_max = calculate_triangle_area(max_a, max_b, max_c)

print("\nРезультаты:")
if area_min is not None:
    print(f"Площадь треугольника из минимальных элементов: {area_min:.2f}")
else:
    print("Из минимальных элементов нельзя составить треугольник")

if area_max is not None:
    print(f"Площадь треугольника из максимальных элементов: {area_max:.2f}")
else:
    print("Из максимальных элементов нельзя составить треугольник")