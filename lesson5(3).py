# 3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
# Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников. Выполнить
# подсчет средней величины дохода сотрудников.

with open('lesson3.txt', 'r', encoding="utf-8") as my_file:
    av_income = []
    salary = []
    my_list = my_file.read().split('\n')
    for i in my_list:
        i = i.split()
        if int(i[1]) < 20000:
            salary.append(i[0])
        av_income.append(i[1])
print(f'Оклад > 20.000 = {salary}\nСредний оклад = {sum(map(int, av_income)) / len(av_income)}')