# 3. Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname,
# position (должность), income (доход).
# Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы:
# оклад и премия, например, {"wage": wage, "bonus": bonus}.
# Создать класс Position (должность) на базе класса Worker. В классе Position реализовать методы получения
# полного имени сотрудника (get_full_name)
# и дохода с учетом премии (get_total_income). Проверить работу примера на реальных данных
# (создать экземпляры класса Position, передать данные,
# проверить значения атрибутов, вызвать методы экземпляров).

class Worker:
    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = income


class Position(Worker):
    def __init__(self, name, surname, position, income):
        Worker.__init__(self, name, surname, position, income)

    def get_full_name(self):
        print(f'Full name: {self.name} {self.surname}')

    def get_total_income(self):
        print(f'Total Income: {sum(self._income.values())}')


chef = Position('Ivan', 'Ivanov', 'Chef', {'wage': 1000, 'bonus': 500})
print(chef.name)
print(chef.surname)
print(chef.position)
print(chef._income)

chef.get_full_name()
chef.get_total_income()

print('\n')

scientist = Position('Pyotr', 'Petrov', 'Scientist', {'wage': 3000, 'bonus': 1000})
print(scientist.name)
print(scientist.surname)
print(scientist.position)
print(scientist._income)

scientist.get_full_name()
scientist.get_total_income()
