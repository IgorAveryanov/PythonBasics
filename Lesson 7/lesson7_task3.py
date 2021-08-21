# 3. Реализовать программу работы с органическими клетками, состоящими из ячеек. Необходимо создать класс Клетка.
# В его конструкторе инициализировать параметр, соответствующий количеству ячеек клетки (целое число).
# В классе должны быть реализованы методы перегрузки арифметических операторов:
# сложение (__add__()), вычитание (__sub__()), умножение (__mul__()), деление (__truediv__()). 
# Данные методы должны применяться только к клеткам и выполнять увеличение, уменьшение, умножение и целочисленное
# (с округлением до целого) деление клеток, соответственно.
# Сложение. Объединение двух клеток. При этом число ячеек общей клетки должно равняться
# сумме ячеек исходных двух клеток.
# Вычитание. Участвуют две клетки. Операцию необходимо выполнять только если разность количества ячеек двух клеток
# больше нуля, иначе выводить соответствующее сообщение.
# Умножение. Создается общая клетка из двух. Число ячеек общей клетки определяется как произведение количества ячеек
# этих двух клеток.
# Деление. Создается общая клетка из двух. Число ячеек общей клетки определяется как целочисленное деление количества
# ячеек этих двух клеток.
# В классе необходимо реализовать метод make_order(), принимающий экземпляр класса и количество ячеек в ряду.
# Данный метод позволяет организовать ячейки по рядам.
# Метод должен возвращать строку вида *****\n*****\n*****..., где количество ячеек между \n равно переданному
# аргументу. Если ячеек на формирование ряда не хватает, то в последний ряд записываются все оставшиеся.
# Например, количество ячеек клетки равняется 12, количество ячеек в ряду — 5.
# Тогда метод make_order() вернет строку: *****\n*****\n**.
# Или, количество ячеек клетки равняется 15, количество ячеек в ряду — 5.
# Тогда метод make_order() вернет строку: *****\n*****\n*****.
# Подсказка: подробный список операторов для перегрузки доступен по ссылке.

class Cell:
    def __init__(self, cell_name, box_number):
        self.cell_name = cell_name
        self.box_number = box_number

    def __add__(self, other):
        self.cell_name = 'Addition: Result cell has'
        return Cell(self.cell_name, self.box_number + other.box_number)

    def __sub__(self, other):
        self.cell_name = 'Subtraction: Result cell has'
        if self.box_number > other.box_number:
            return Cell(self.cell_name, self.box_number - other.box_number)
        else:
            return f'Subtraction: cell_1 has fewer boxes than cell_2. Result is negative'

    def __mul__(self, other):
        self.cell_name = 'Multiplication: Result cell has'
        return Cell(self.cell_name, self.box_number * other.box_number)

    def __floordiv__(self, other):
        self.cell_name = 'Floor Division: Result cell has'
        return Cell(self.cell_name, self.box_number // other.box_number)

    def make_order(self, boxes_in_row):
        self.boxes_in_row = boxes_in_row
        print(f'\nOrdered cell ({boxes_in_row} boxes in row): ')
        for i in range(self.box_number // self.boxes_in_row):
            print('*' * self.boxes_in_row)
        print('*' * (self.box_number % self.boxes_in_row))

    def __str__(self):
        return f'{self.cell_name} has {self.box_number} boxes'


cell_1 = Cell('cell_1', 12)
print(cell_1)
cell_2 = Cell('cell_2', 8)
print(cell_2)
print(cell_1 + cell_2)
print(cell_1 - cell_2)
print(cell_1 * cell_2)
print(cell_1 // cell_2)
cell_1.make_order(5)
