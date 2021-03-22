# 2. Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества
# строк, количества слов в каждой строке.


num_words = 0
num_lines = 0

with open("lesson2.txt", "r", encoding="utf-8") as s_file:
    for line in s_file:
        words = line.split()
        num_lines += 1
        num_words += len(words)
    print(f'Number of words = {num_words}\nNumber of lines = {num_lines}')

