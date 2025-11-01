#Создаем класс Car с атрибутами марка и модель
class Car:
    #Конструктор класса, который инициализирует атрибуты класса Car
    def __init__(self, make, model):
        self.make = make
        self.model = model

#Создание экземпляра класса с помощью конструктора описанного выше
my_car = Car('Toyota', 'Corolla')