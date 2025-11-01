from lab_work.lab_8.lab2_8 import Car

#Создаем класс ElectricCar
class ElectricCar(Car):
    #Конструктор, который заимствует атрибуты суперкласса (родителя) и добавляет новый атрибут - объем батареи
    def __init__(self, make, model, battery_capacity):
        super().__init__(make, model)
        self.battery_capacity = battery_capacity

    #Новый метод charge
    def charge(self):
        print(f"Charging the {self.make} {self.model} with {self.battery_capacity} kWh")

#Создание экземпляра класса
my_electric_car = ElectricCar("Tesla", "Model S", 75)
#Вызов метода унаследованного от родительского класса
my_electric_car.drive()
#Вызов метода нового созданного класса
my_electric_car.charge()