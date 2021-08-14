# 5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
from random import randint

with open("text_5.txt", 'w') as t_5:
    numbers_list = [randint(-100, 101) for number in range(10)]  # Генерируем список случайных чисел
    for number in numbers_list:
        print(number, file=t_5)

with open("text_5.txt", 'r') as t_5:
    numbers_list = t_5.readlines()
    numbers_list = [number.rstrip() for number in numbers_list]
    print(f'Набор чисел из файла: {list(map(int, numbers_list))}')  # Печатаем созданный в файле список
    print(f'Сумма набора чисел равна: {sum(list(map(int, numbers_list)))}')  # Печатаем сумму чисел


