# Продолжить работу над заданием. В программу должна попадать строка из слов, разделённых пробелом.
# Каждое слово состоит из латинских букв в нижнем регистре.
# Нужно сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы.
# Используйте написанную ранее функцию int_func().

def filter_function(user_phrase):
    """ Функция фильтрует введенную пользователем строку слов,
    оставляя только слова, состоящие из строчных латинских букв"""
    filtered_user_phrase = []
    i = 0
    for word in user_phrase:
        for letter in word:
            if letter not in alphabet:
                user_phrase[i] = 'deleted'  # Заменяем все нелатинские слова на 'deleted'
                break
        i += 1
    for word in user_phrase:
        if word != 'deleted':
            filtered_user_phrase.append(word)  # Создаем новый список слов без 'deleted'

    filtered_user_phrase = list(filter(str.islower, filtered_user_phrase))  # Удаляем все слова с большими буквами

    return filtered_user_phrase


def init_func(user_phrase):
    """Функция озаглавливает каждое из оставшихся слов"""
    capitalized_phrase = list(map(lambda word: word.capitalize(), user_phrase))
    return capitalized_phrase


alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
user_phrase = input('Введите фразу строчными латинскими буквами: ').split(' ')
filtered_user_phrase = filter_function(user_phrase)
new_phrase = ' '.join(init_func(filtered_user_phrase))
print(f'Результат: {new_phrase}')
