#Создаем класс Car с атрибутами марка и модель
class Car:
    #Конструктор класса, который инициализирует атрибуты класса Car
    def __init__(self, make, model):
        self._make = make #Защищенный атрибут
        self.__model = model #Приватный атрибут

    #Создание метода
    def drive(self):
        print(f"Driving the {self._make} {self.__model}")

#Создание экземпляра класса с помощью конструктора описанного выше
my_car = Car('Toyota', 'Corolla')
print(my_car._make) #Доступ к защищенному атрибуту
# print(my_car.__model) #Ошибка! Приватный атрибут не доступен
my_car.drive() #Вызов метода "drive"