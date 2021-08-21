# 1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
# который должен принимать данные (список списков) для формирования матрицы.
# Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
# Примеры матриц вы найдете в методичке.
# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix
# (двух матриц). Результатом сложения должна быть новая матрица.
# Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы
# складываем с первым элементом первой строки второй матрицы и т.д.

import random


class Matrix:
    def __init__(self, matrix):
        self.random_matrix = matrix

    def __str__(self):
        # печатаем матрицу красиво
        return f"\n{chr(10).join(chr(9).join(map(str, row)) for row in self.random_matrix)}"

    def __add__(self, other):
        # проверяем равнозначность размеров двух матриц и суммируем поэлементно в случае положительного ответа
        if len(self.random_matrix) == len(other.random_matrix) and \
           len(self.random_matrix[0]) == len(other.random_matrix[0]):
            result = [list(map(sum, zip(*i))) for i in zip(self.random_matrix, other.random_matrix)]
            return Matrix(result)
        else:
            return f'Addition is impossible! Matrices have to be the same size'


print('Enter range of random numbers for matrices: ')
range_start, range_end = map(int, input().split())

print('\nEnter number of rows and columns for 1st matrix: ')
n1, m1 = map(int, input().split())
matrix = [[random.randint(range_start, range_end) for _ in range(n1)] for _ in range(m1)]
matrix_1 = Matrix(matrix)

print('\nEnter number of rows and columns for 2nd matrix: ')
n2, m2 = map(int, input().split())
matrix = [[random.randint(range_start, range_end) for _ in range(n2)] for _ in range(m2)]
matrix_2 = Matrix(matrix)

print(f'\nRandom matrix 1: {matrix_1}')
print(f'Random matrix 2: {matrix_2}')

print(f'Result matrix: {matrix_1 + matrix_2}')
