# 1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые
# пользователем. Об окончании ввода данных свидетельствует пустая строка.


with open("lesson1.txt", "w", encoding="utf-8") as txtfile:
    while True:
        line = input("Enter some text ")
        if not line:
            break
    print(line, file=txtfile)
