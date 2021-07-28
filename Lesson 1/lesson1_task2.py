# Пользователь вводит время в секундах.
# Переведите время в часы, минуты, секунды и выведите в формате чч:мм:сс.
# Используйте форматирование строк.

user_seconds = int(input("Введите число секунд: "))
hours = user_seconds // 3600
minutes = user_seconds % 3600 // 60
seconds = user_seconds % 3600 % 60
print(f'Прошло {hours:02d}:{minutes:02d}:{seconds:02d}')
