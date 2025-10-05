from for_import import heron_formula

a = float(input("Введите длину первой стороны треугольника: "))
b = float(input("Введите длину второй стороны треугольника: "))
c = float(input("Введите длину третьей стороны треугольника: "))
area = heron_formula(a, b, c)
print(f"Площадь треугольника: {area}")