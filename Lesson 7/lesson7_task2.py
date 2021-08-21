# 2. Реализовать проект расчета суммарного расхода ткани на производство одежды.
# Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
# К типам одежды в этом проекте относятся пальто и костюм.
# У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
# Это могут быть обычные числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
# для костюма (2 * H + 0.3). Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания: реализовать
# абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.

from abc import ABC, abstractmethod


class Clothes(ABC):

    def __init__(self, p):
        self.param = p

    @abstractmethod
    def expenses(self):
        pass

    def __str__(self):
        return self.param


class Coat(Clothes):

    def __str__(self):
        return f"Пальто {self.param} размера"

    @property
    def expenses(self):
        return f'Нужно ткани на пальто: {round(self.param / 6.5) + 0.5}'


class Suit(Clothes):

    def __str__(self):
        return f'Костюм ростом {self.param} м'

    @property
    def expenses(self):
        return f'Нужно ткани на костюм: {self.param * 2 + 0.3}'


a = Coat(48)
b = Suit(1.9)
print(a)
print(a.expenses)
print(b)
print(b.expenses)
