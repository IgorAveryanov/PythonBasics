# 2. Создать текстовый файл (не программно), сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке.

with open("text_2.txt", "r", encoding="utf-8") as t_2:
    line_counter = 0
    text = t_2.readlines()
    text = [line.rstrip() for line in text]
    for line in text:
        word_counter = 0
        for word in line.split():
            if word != '—':
                word_counter += 1
        print(line, end='')
        print(f'  (слов в строке: {word_counter})')
        line_counter += 1
    print(f'\nВсего строк: {line_counter}')
