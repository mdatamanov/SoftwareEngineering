# Базовый класс для всех геометрических фигур
class Shape:
    def area(self):
        # Метод должен быть переопределен в дочерних классах
        pass


# Класс Прямоугольник, наследуется от Shape
class Rectangle(Shape):
    def __init__(self, width, height):
        # Инициализация ширины и высоты прямоугольника
        self.width = width
        self.height = height

    def area(self):
        # Реализация метода area для прямоугольника
        # Площадь = ширина × высота
        return self.width * self.height


# Класс Круг, наследуется от Shape
class Circle(Shape):
    def __init__(self, radius):
        # Инициализация радиуса круга
        self.radius = radius

    def area(self):
        # Реализация метода area для круга
        # Площадь = π × радиус² (π ≈ 3.14)
        return 3.14 * self.radius * self.radius


# Демонстрация полиморфизма
if __name__ == "__main__":
    # Создаем массив (список) фигур
    shapes = []

    # Добавляем прямоугольник в массив
    rectangle = Rectangle(5, 3)  # Прямоугольник 5x3
    shapes.append(rectangle)

    # Добавляем круг в массив
    circle = Circle(4)  # Круг с радиусом 4
    shapes.append(circle)

    # Выводим площади всех фигур в массиве
    print("Площади фигур:")
    for shape in shapes:
        # Полиморфизм: вызывается правильный метод area()
        # в зависимости от типа объекта
        area = shape.area()
        # Определяем тип фигуры для красивого вывода
        if isinstance(shape, Rectangle):
            print(f"Прямоугольник: {area}")
        elif isinstance(shape, Circle):
            print(f"Круг: {area}")