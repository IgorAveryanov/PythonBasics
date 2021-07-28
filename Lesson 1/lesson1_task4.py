# Пользователь вводит целое положительное число.
# Найдите самую большую цифру в числе. 
# Для решения используйте цикл while и арифметические операции.

user_number = int(input("Введите целое положительное число: "))

while user_number < 0:
    print('Вы ввели отрицательное число! Попробуйте ещё раз ')
    user_number = int(input("\nВведите целое положительное число: "))

max_digit = user_number % 10
user_number //= 10

while user_number > 0:
    if user_number % 10 > max_digit:
        max_digit = user_number % 10
    user_number //= 10
print(f'Самая большая цифра в этом числе: {max_digit}')
