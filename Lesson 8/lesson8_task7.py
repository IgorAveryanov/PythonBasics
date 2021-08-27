# 7. Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число»,
# реализуйте перегрузку методов сложения и умножения комплексных чисел. Проверьте работу проекта,
# создав экземпляры класса (комплексные числа) и выполнив сложение и умножение созданных экземпляров.
# Проверьте корректность полученного результата.

class ComplexNumbers:
    def __init__(self, r, i):
        self.r = r
        self.i = i
        self.number = complex(r, i)

    def __add__(self, other):
        return ComplexNumbers(self.r + other.r, self.i + other.i)

    def __mul__(self, other):
        return ComplexNumbers(self.r * other.r - self.i * other.i, self.r * other.i + self.i * other.r)

    def __str__(self):
        return f"{self.number}"


a = ComplexNumbers(1, 2)
print(a.number)
b = ComplexNumbers(3, 4)
print(b.number)
print(a+b)
print(a*b)
