# -*- coding: utf-8 -*-


class Base(object):  # Наслідування від object
    def __init__(self):
        print(1)

    def b(self):
        print(2)


class One(Base):  # Наслідування від object через Base
    def __init__(self):
        # Викликаємо конструктор базового класу
        super(One, self).__init__()
        # Викликаємо метод b() базового класу
        super(One, self).b()
        # Викликаємо метод b() класу One явно
        One.b(self)
        # Виводимо "3"
        print(3)

    def b(self):
        print(4)


class Demo(object):  # Наслідування від object
    def main(self):
        One()


# Тестування
demo = Demo()
demo.main()


