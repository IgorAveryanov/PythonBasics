# 5. Реализовать класс Stationery (канцелярская принадлежность). Определить в нем атрибут title (название)
# и метод draw (отрисовка).
# Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка),
# Pencil (карандаш), Handle (маркер).
# В каждом из классов реализовать переопределение метода draw. Для каждого из классов методы
# должен выводить уникальное сообщение.
# Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.

class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print(f'Запуск отрисовки\n')


class Pen(Stationery):

    def draw(self):
        print(f'Рисуем ручкой\n')


class Pencil(Stationery):

    def draw(self):
        print(f'Рисуем карандашом\n')


class Handle(Stationery):

    def draw(self):
        print(f'Рисуем маркером\n')


stationery = Stationery('Канцелярская принадлежность')
print(stationery.title)
stationery.draw()

pen = Pen('Ручка')
print(pen.title)
pen.draw()

pencil = Pencil('Карандаш')
print(pencil.title)
pencil.draw()

handle = Handle('Маркер')
print(handle.title)
handle.draw()
