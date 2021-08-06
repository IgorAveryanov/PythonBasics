# Реализовать функцию my_func(), которая принимает три позиционных аргумента
# и возвращает сумму наибольших двух аргументов.

def my_func(x, y, z):
    list_of_digits = [x, y, z]
    list_of_digits.sort()
    return list_of_digits[1] + list_of_digits[2]
    
    
a, b, c = float(input('Введите первое число: ')), float(input('Введите второе число: ')), \
          float(input('Введите третье число: '))
print(f'Сумма двух наибольших из введенных чисел равна: {my_func(a, b, c)}')
   
