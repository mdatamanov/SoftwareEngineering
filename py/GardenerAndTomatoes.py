class Tomato:
    states = ['отсутствует', 'цветение', 'зеленый', 'красный']
    def __init__(self, _index):
        self._index = _index
        self._state = Tomato.states[0]
    #Атрибуты являются приватными (доступными только для класса "Tomato")

    def grow(self):
        current_index = Tomato.states.index(self._state)
        if current_index < len(Tomato.states) - 1:
            self._state = Tomato.states[current_index + 1]

    def is_ripe(self):
        return self._state == 'красный'

class TomatoBush:
    def __init__(self, count):
        self.tomatoes = [Tomato(i) for i in range(1, count + 1)]

    def grow_all(self):
        for tomato in self.tomatoes:
            tomato.grow()

    def all_are_ripe(self):
        return all(tomato.is_ripe() for tomato in self.tomatoes)

    def give_away_all(self):
        self.tomatoes.clear()
        print('список томатов после сбора урожаев очищен')

class Gardener:
    def __init__(self, name, _plant):
        self.name = name
        self._plant = _plant
        #Name - публичное, _plant - приватное

    def work(self):
        print(f"{self.name} ухаживает за растениями...")
        self._plant.grow_all()

    def harvest(self):
        if self._plant.all_are_ripe():
            print(f"{self.name} собирает урожай!")
            self._plant.give_away_all()
            return True
        else:
            print("Предупреждение: еще не все томаты созрели!")
            return False

    @staticmethod
    def knowledge_base():
        print("\n=== СПРАВКА ПО САДОВОДСТВУ ===")
        print("1. Томаты проходят 4 стадии созревания: отсутствует, цветение, зеленый, красный")
        print("2. Садовник должен ухаживать за растениями, чтобы они росли")
        print("3. Урожай можно собрать только когда все томаты стали красными")
        print("4. После сбора урожая томаты удаляются из куста")
        print("5. Продолжайте ухаживать за растениями, пока все томаты не созреют")
        print("===============================\n")


if __name__ == "__main__":
    Gardener.knowledge_base()

    bush = TomatoBush(3)  # Куст с 3 томатами
    gardener = Gardener("Иван", bush)

    print(f"Создан садовник: {gardener.name}")
    print(f"Создан куст с {len(bush.tomatoes)} томатами")

    print("\n--- Первый уход ---")
    gardener.work()

    print("\n--- Попытка сбора урожая 1 ---")
    gardener.harvest()

    print("\n--- Второй уход ---")
    gardener.work()

    print("\n--- Третий уход ---")
    gardener.work()

    print("\n--- Финальная попытка сбора урожая ---")
    success = gardener.harvest()

    if success:
        print("\n Программа завершена успешно! Урожай собран!")
    else:
        print("\n Нужно продолжать ухаживать за растениями!")






