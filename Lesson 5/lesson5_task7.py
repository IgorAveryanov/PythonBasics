# 7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме:
# название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
# Если фирма получила убытки, в расчет средней прибыли ее не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
# Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
#
# Подсказка: использовать менеджеры контекста.
import json

with open("text_7.txt", "r", encoding="utf-8") as t_7:
    firms_list = t_7.readlines()
    firms_list = [firm.rstrip().split() for firm in firms_list]
    for name in firms_list:
        name[2], name[3] = int(name[2]), int(name[3])

    name_list = [name[0] for name in firms_list]  # Список названий фирм
    profit_list = [(name[2] - name[3]) for name in firms_list]  # Список прибылей
    data_dict = dict(zip(name_list, profit_list))  # Словарь названий и прибылей
    print(f'Словарь названий и прибылей: {data_dict}')

    summ = 0
    count = 0
    for profit in profit_list:
        if profit > 0:
            summ += profit
            count += 1
    average_profit = summ / count  # Высчитываем среднюю прибыль БЕЗ убыточных фирм

    profit_dict = {"average_profit": average_profit}
    print(f'Словарь средней прибыли: {profit_dict}')

    result_list = [data_dict, profit_dict]  # Итоговый список
    print(f'Результирующий словарь: {result_list}')

with open("text_77.json", "w", encoding="utf-8") as t_77:
    json.dump(result_list, t_77, ensure_ascii=False, indent=2)
