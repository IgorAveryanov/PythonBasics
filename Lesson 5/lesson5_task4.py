# 4. Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Напишите программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.

rus_number_list = ['Один', 'Два', 'Три', 'Четыре']

with open("text_4.txt", "r", encoding="utf-8") as t_4:
    number_list = t_4.readlines()
    number_list = [number.rstrip().split() for number in number_list]

for i in range(len(number_list)):
    number_list[i][0] = rus_number_list[i]  # Заменяем английские числительные на русские
    number_list[i] = ' '.join(number_list[i])

with open("text_4_output.txt", "w", encoding="utf-8") as t_4_output:
    for i in range(len(number_list)):
        print(number_list[i], end='\n', file=t_4_output)
