# Реализовать скрипт, в котором должна быть предусмотрена функция расчёта заработной платы сотрудника.
# Используйте в нём формулу: (выработка в часах*ставка в час) + премия.
# Во время выполнения расчёта для конкретных значений необходимо запускать скрипт с параметрами.

from sys import argv

try:
    script_name, output, hour_rate, bonus = argv
    if len(argv) != 4:
        raise ValueError
    argv = list(map(float, argv[1:]))
    for arg in argv:
        if arg < 0:
            raise ValueError
    print(f'Выработка: {output} ч., ставка: {hour_rate} руб./ч, премия: {bonus} руб.')
    print(f'Заработная плата: {argv[0] * argv[1] + argv[2]} руб.')
except ValueError:
    print("Ошибка! Введите только 4 параметра (выработка, ставка и премия должны быть положительными числами)!")
