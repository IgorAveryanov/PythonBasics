# Реализовать функцию int_func(), принимающую слова из маленьких латинских букв 
# и возвращающую их же, но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.

def init_func(word):
    # Озаглавливаем слово
    return word.capitalize()


alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
user_word = ''

# Проверка введенного слова на соответствие условиям задачи
do = True
while do:
    user_word = input('Введите слово строчными латинскими буквами: ')
    for letter in user_word:
        if letter not in alphabet:
            print('Ошибка! Только латинские буквы!\n')
            break
        elif not user_word.islower():
            print('Ошибка! Только маленькие латинские буквы!\n')
            break
        else:
            do = False

print(f'Слово с прописной первой буквой: {init_func(user_word)}')
