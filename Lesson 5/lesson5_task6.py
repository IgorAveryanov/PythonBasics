# 6. Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет
# и наличие лекционных, практических и лабораторных занятий по этому предмету и их количество.
# Важно, чтобы для каждого предмета не обязательно были все типы занятий.
# Сформировать словарь, содержащий название предмета и общее количество занятий по нему. Вывести словарь на экран.
# Примеры строк файла:
# Информатика: 100(л) 50(пр) 20(лаб).
# Физика: 30(л) — 10(лаб)
# Физкультура: — 30(пр) —
#
# Пример словаря:
# {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
import re

with open("text_6.txt", "r", encoding="utf-8") as t_6:
    subject_list = t_6.readlines()
    subject_list = [subject.rstrip().split(':') for subject in subject_list]  # Делим считанное по символу ':'

    subject_name_list = [subject[0] for subject in subject_list]  # Формируем список предметов
    print(f'Список предметов: {subject_name_list}')

    hours_list = [subject[1] for subject in subject_list]  # Формируем список часов
    hours_list = [re.findall('\d+', hour) for hour in hours_list]  # Отделили цифры от других символов
    hours_list = [list(map(int, hour)) for hour in hours_list]  # Преобразовали в int
    hours_list = [list(map(sum, hours_list))]  # Просуммировали
    hours_list = [item for sublist in hours_list for item in sublist]  # Извлекли список из списка
    print(f'Список суммарных часов по каждому предмету: {hours_list}')

    subject_data = dict(zip(subject_name_list, hours_list))  # Сшили в словарь
    print(f'Результирующий словарь: {subject_data}')
