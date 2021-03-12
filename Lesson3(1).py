# 1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.

def my_func(*args):
    try:
        arg1 = int(input("input first number"))
        arg2 = int(input("input second number"))
        res = arg1 / arg2
    except ZeroDivisionError:
        return "division by zero"
    except ValueError:
        return "No value"

print("def can't be 'Number/0'")