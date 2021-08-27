# 3. Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел.
# Проверить работу исключения на реальном примере. Необходимо запрашивать у пользователя данные и заполнять список.
# Класс-исключение должен контролировать типы данных элементов списка.
# Примечание: длина списка не фиксирована. Элементы запрашиваются бесконечно,
# пока пользователь сам не остановит работу скрипта, введя, например, команду “stop”.
# При этом скрипт завершается, сформированный список выводится на экран.
# Подсказка: для данного задания примем, что пользователь может вводить только числа и строки.
# При вводе пользователем очередного элемента необходимо реализовать проверку типа элемента и вносить его в список,
# только если введено число. Класс-исключение должен не позволить пользователю ввести текст (не число) и
# отобразить соответствующее сообщение. При этом работа скрипта не должна завершаться.

class DataTypeError(Exception):
    def __init__(self, txt):
        self.txt = txt


def list_function():
    numbers_list = []
    while True:
        string_numbers = input('Введите числа через пробел (stop - для выхода): ').lower().split(' ')
        try:
            for word in string_numbers:
                for letter in word:
                    if letter == '_':
                        raise DataTypeError('!!!!!')
            if 'stop' in string_numbers:
                idx = string_numbers.index('stop')
                user_list = list(map(float, string_numbers[:idx]))
                for number in user_list:
                    numbers_list.append(number)
                break
            else:
                user_list = list(map(float, string_numbers))
                for number in user_list:
                    numbers_list.append(number)
        except (ValueError, DataTypeError) as err:
            print(f'{err}\n')
    print(f'Итоговый список: {numbers_list}')


list_function()
