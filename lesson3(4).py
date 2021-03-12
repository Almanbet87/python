# 4. Программа принимает действительное положительное число x и целое отрицательное число y. Необходимо
# выполнить возведение числа x в степень y. Задание необходимо реализовать в виде функции my_func(x, y).
# При решении задания необходимо обойтись без встроенной функции возведения числа в степень.
#
# Подсказка: попробуйте решить задачу двумя способами. Первый — возведение в степень с помощью оператора
# **. Второй — более сложная реализация без оператора **, предусматривающая использование цикла.

def my_func(x, y):
    return x **y

print(f'result {my_func(int(input("enter positive number x = ")), int(input("enter a negative degree y = ")))}')

...

def my_func(x, y):
    return x * pow(x, y-1)

print(f'result {my_func(int(input("enter positive number x = ")), int(input("enter a negative degree y = ")))}')



