# 4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника»,
# который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определить параметры, общие для приведенных типов. В классах-наследниках реализовать параметры,
# уникальные для каждого типа оргтехники.
# 5. Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники на склад и передачу
# в определенное подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники,
# а также других данных, можно использовать любую подходящую структуру, например словарь.
# 6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных.
# Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
# Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники» максимум возможностей,
# изученных на уроках по ООП.


class MenuError(Exception):
    def __init__(self, txt):
        self.txt = txt


class DeviceTypeError(Exception):
    def __init__(self, txt):
        self.txt = txt


class PriceTypeError(Exception):
    def __init__(self, txt):
        self.txt = txt


class DataTypeError(Exception):
    def __init__(self, txt):
        self.txt = txt


class ParamNumberError(Exception):
    def __init__(self, txt):
        self.txt = txt


class Department:
    """класс Отдел (Подразделение), куда можно передавать предметы со склада"""

    def __init__(self):
        self.department = []

    def add(self, item):
        self.department.append(item)

    def __str__(self):
        p, s, x = 0, 0, 0

        for item in self.department:
            if item.device == 'Принтер':
                p += 1
            elif item.device == 'Сканер':
                s += 1
            elif item.device == 'Ксерокс':
                x += 1

        return f"В отделе сейчас {len(self.department)} устройств ({p} принтеров, {s} сканеров, {x} ксероксов)"


# класс Склад
class Storage:
    """
    Класс Склад. Можно добавлять устройства (оргтехнику) методом add(), удалять их методом delete(),
    перемещать в другой Отдел методом transfer(),
    подсчитать общую стоимость хранящихся устройств методом summ()
    """

    def __init__(self):
        self.storage = []

    def add(self, item):
        self.storage.append(item)

    def delete(self, index):
        print(
            f'Удаляем {self.storage[index].device} {self.storage[index].vendor} {self.storage[index].model} со склада')
        del self.storage[index]

    def transfer(self, index):
        print(
            f'Перемещаем {self.storage[index].device} {self.storage[index].vendor} {self.storage[index].model} со склада в отдел')
        department.add(self.storage[index])
        del self.storage[index]

    def summ(self):
        total_value = 0
        for item in self.storage:
            total_value += item.price
        print(f'Общая стоимость устройств на складе: {total_value}')

    def __str__(self):
        p, s, x = 0, 0, 0
        for item in self.storage:
            if item.device == 'Принтер':
                p += 1
            elif item.device == 'Сканер':
                s += 1
            elif item.device == 'Ксерокс':
                x += 1
        return f"На складе сейчас {len(self.storage)} устройств (принтеры: {p} шт., сканеры {s} шт., ксероксы: {x} шт.)"


class OfficeEquipment:
    device = 'Оргтехника'

    def __init__(self, vendor, model, price):
        self.vendor = vendor
        self.model = model
        self.price = price

    def __str__(self):
        return f"{self.device} {self.vendor} {self.model} ({self.price})"


class Printer(OfficeEquipment):
    device = 'Принтер'

    def __init__(self, vendor, model, price, is_color):
        super().__init__(vendor, model, price)
        self.is_color = is_color

    def __str__(self):
        return f"{self.device} {self.vendor} {self.model} (цена: {self.price}) (цв./чб: {self.is_color})"


class Scanner(OfficeEquipment):
    device = 'Сканер'

    def __init__(self, vendor, model, price, dpi):
        super().__init__(vendor, model, price)
        self.dpi = dpi

    def __str__(self):
        return f"{self.device} {self.vendor} {self.model} (цена: {self.price}) (разрешение: {self.dpi} dpi)"


class Xerox(OfficeEquipment):
    device = 'Ксерокс'

    def __init__(self, vendor, model, price, cpm):
        super().__init__(vendor, model, price)
        self.cpm = cpm

    def __str__(self):
        return f"{self.device} {self.vendor} {self.model} (цена: {self.price}) (скорость копирования: {self.cpm} копий/мин.)"


def menu():
    print(f'\nМЕНЮ')
    print(f'Введите цифру, соответствующую желаемому действию:')
    print(f'1. Посмотреть, что есть на складе')
    print(f'2. Добавить устройство на склад')
    print(f'3. Удалить устройство со склада')
    print(f'4. Переместить устройство со склада в отдел')
    print(f'5. Посчитать общую стоимость устройств на складе')
    print(f'6. Выйти')


storage = Storage()
department = Department()


def menu_scan_storage():
    """Посмотреть, что есть на складе"""
    print(storage)
    for i, item in enumerate(storage.storage, start=1):
        print(i, item)


def menu_add_to_storage():
    """Добавить устройство на склад"""
    try:
        data_string = input(
            f'Введите через пробел тип устройства (принтер, сканер или ксерокс)'
            f' и характеристики (производитель, модель, цена)')
        data_list = data_string.split()
        if len(data_list) != 4:
            raise ParamNumberError(f'Ошибка! Неправильное число параметров (нужно 4)')
        device, vendor, model, price = data_list[0], data_list[1], data_list[2], data_list[3]
        if not price.isdigit():
            raise PriceTypeError(f'Ошибка! Цена должна быть целым положительным числом')
        if device.lower() == 'принтер':
            is_color = input('Цветной(введите "1") или черно-белый(введите "2")?')
            if is_color == '1':
                is_color = 'цветной'
            elif is_color == '2':
                is_color = 'черно-белый'
            else:
                raise DataTypeError(f'Ошибка! Должно быть положительное целое число')
            n = input('Сколько шт.?')
            if not n.isdigit():
                raise DataTypeError(f'Ошибка! Должно быть положительное целое число')
            for i in range(int(n)):
                storage.add(Printer(vendor, model, float(price), is_color))
            print(f'Устройства отправлены на склад!')
        elif device.lower() == 'сканер':
            dpi = input('Разрешение dpi?')
            if not dpi.isdigit():
                raise DataTypeError(f'Ошибка! Должно быть положительное целое число')
            n = input('Сколько шт.?')
            if not n.isdigit():
                raise DataTypeError(f'Ошибка! Должно быть положительное целое число')
            for i in range(int(n)):
                storage.add(Scanner(vendor, model, float(price), int(dpi)))
            print(f'Устройства отправлены на склад!')
        elif device.lower() == 'ксерокс':
            cpm = input('Скорость копирования?')
            if not cpm.isdigit():
                raise DataTypeError(f'Ошибка! Должно быть положительное целое число')
            n = input('Сколько шт.?')
            if not n.isdigit():
                raise DataTypeError(f'Ошибка! Должно быть положительное целое число')
            for i in range(int(n)):
                storage.add(Xerox(vendor, model, float(price), cpm))
            print(f'Устройства отправлены на склад!')
        else:
            raise DeviceTypeError(f'Ошибка! Принимаем только "принтер", "сканер", "ксерокс"!')
    except (DeviceTypeError, PriceTypeError, DataTypeError, ParamNumberError) as err:
        print(err)


def delete_from_storage():
    """Удалить устройство со склада"""
    if not storage.storage:
        print('Склад пуст. Удалять нечего')
    else:
        print(f'\nСписок устройств на складе:')
        for i, item in enumerate(storage.storage, start=1):
            print(i, item)
        index = int(input(f'Введите номер устройства, которое нужно удалить:')) - 1
        storage.delete(index)


def transfer():
    """Переместить устройство со склада в отдел"""
    if not storage.storage:
        print('Склад пуст. Перемещать нечего')
    else:
        print(f'\nСписок устройств на складе:')
        for i, item in enumerate(storage.storage, start=1):
            print(i, item)
        index = int(input(f'Введите номер устройства, которое нужно передать в Отдел:')) - 1
        storage.transfer(index)


def main():
    while True:
        try:
            menu()
            user_choice = input()
            # 1. Посмотреть что на складе
            if user_choice == '1':
                menu_scan_storage()
            # 2. Добавить устройство на склад        
            elif user_choice == '2':
                menu_add_to_storage()
            # 3. Удалить устройство со склада     
            elif user_choice == '3':
                delete_from_storage()
            # 4. Переместить устройство со склада в отдел 
            elif user_choice == '4':
                transfer()
            # 5. Посчитать общую стоимость устройств на складе   
            elif user_choice == '5':
                storage.summ()
            # 6. Выйти
            elif user_choice == '6':
                print('Заканчиваем программу')
                break
            else:
                raise MenuError('Ошибка! Введите число от 1 до 6')
        except MenuError as err:
            print(err)


main()
