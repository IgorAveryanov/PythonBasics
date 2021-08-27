# 1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки
# формата «день-месяц-год».
# В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать число, месяц, год
# и преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию
# числа, месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.

class Date:
    def __init__(self, d, m, y):
        self.day = d
        self.month = m
        self.year = y

    @classmethod
    def extract(cls, date):
        date = date.split('-')
        d, m, y = int(date[0]), int(date[1]), int(date[2])
        cls.valid(d, m, y)
        print('Форматированная дата:', end=' ')
        for item in date:
            print(item, end=' ')
        print('\n')
        return cls(d, m, y)

    @staticmethod
    def valid(d, m, y):
        if 1 <= d <= 31:
            if 1 <= m <= 12:
                if 0 <= y <= 9999:
                    print("Валидация успешна!")
                else:
                    print("Год неправильный! (0-9999)")
            else:
                print("Месяц неправильный! (1-12)")
        else:
            print("День неправильный! (1-31)")


date_example = Date.extract('28-02-2021')
date_example_2 = Date.extract('33-02-2021')
date_example_3 = Date.extract('28-13-2021')
date_example_4 = Date.extract('28-02-10000')

