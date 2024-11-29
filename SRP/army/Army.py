from abc import ABC, abstractmethod


# Базовий клас солдата
class Soldier(ABC):
    def __init__(self, name, army_type, specialization):
        self.name = name
        self.army_type = army_type
        self.specialization = specialization

    def introduce(self):
        return f"{self.specialization} {self.name}, {self.army_type} {self.__class__.__name__.lower()}"


# Конкретні класи солдатів
class Swordsman(Soldier):
    pass


class Lancer(Soldier):
    pass


class Archer(Soldier):
    pass


# Абстрактна фабрика для армій
class Army(ABC):
    @abstractmethod
    def train_swordsman(self, name):
        pass

    @abstractmethod
    def train_lancer(self, name):
        pass

    @abstractmethod
    def train_archer(self, name):
        pass


# Європейська армія
class EuropeanArmy(Army):
    def train_swordsman(self, name):
        return Swordsman(name, "European", "Knight")

    def train_lancer(self, name):
        return Lancer(name, "European", "Raubritter")

    def train_archer(self, name):
        return Archer(name, "European", "Ranger")


# Азіатська армія
class AsianArmy(Army):
    def train_swordsman(self, name):
        return Swordsman(name, "Asian", "Samurai")

    def train_lancer(self, name):
        return Lancer(name, "Asian", "Ronin")

    def train_archer(self, name):
        return Archer(name, "Asian", "Shinobi")


# Основна програма
def main():
    # Створення армій
    my_army = EuropeanArmy()
    enemy_army = AsianArmy()

    # Тренування європейських солдатів
    soldier_1 = my_army.train_swordsman("Jaks")
    soldier_2 = my_army.train_lancer("Harold")
    soldier_3 = my_army.train_archer("Robin")

    # Тренування азіатських солдатів
    soldier_4 = enemy_army.train_swordsman("Kishimoto")
    soldier_5 = enemy_army.train_lancer("Ayabusa")
    soldier_6 = enemy_army.train_archer("Kirigae")

    # Виведення опису солдатів
    print(soldier_1.introduce())
    print(soldier_2.introduce())
    print(soldier_3.introduce())
    print(soldier_4.introduce())
    print(soldier_5.introduce())
    print(soldier_6.introduce())


if __name__ == "__main__":
    main()
