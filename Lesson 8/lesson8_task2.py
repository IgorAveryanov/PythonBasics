# 2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
# Проверьте его работу на данных, вводимых пользователем.
# При вводе пользователем нуля в качестве делителя программа должна корректно
# обработать эту ситуацию и не завершиться с ошибкой.

class ZeroDivError(Exception):
    def __init__(self, txt):
        self.txt = txt


while True:
    try:
        a = input(f'Enter first number ("q" for exit): ')
        if a.lower() == 'q':
            print(f'Shutting down now')
            break
        a = float(a)
        b = input(f'Enter second number ("q" for exit): ')
        if b.lower() == 'q':
            print(f'Shutting down now')
            break
        b = float(b)
        if b == 0:
            raise ZeroDivError('Zero Division!')
    except (ValueError, ZeroDivError) as err:
        print(f'Error: {err}\n')
    else:
        print(f'Result: {a/b}\n')
    
