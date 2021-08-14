# 3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
# Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.

with open("text_3.txt", "r", encoding="utf-8") as t_3:
    person_list = t_3.readlines()
    person_list = [person.rstrip() for person in person_list]

print('Сотрудники, получающие менее 20000: ')
for person in person_list:
    if float(person.split()[1]) < 20000:
        print(person.split()[0])

sum = 0
for person in person_list:
    sum += float(person.split()[1])
print(f'\nСредний доход сотрудников:  {sum / len(person_list)}')
