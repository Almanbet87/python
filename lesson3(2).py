# 2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя: имя,
# фамилия, год рождения, город проживания, email, телефон. Функция должна принимать параметры как
# именованные аргументы. Реализовать вывод данных о пользователе одной строкой.

def my_func(name, surname, birthday, city, email, phonenumber):
    return [name, surname, birthday, city, email, phonenumber]

print(
    f'{(input("enter name "), input("enter surname "), int(input("enter birthday ")), input("enter city "), input("enter email "), int(input("enter phonenumber ")))}'
      )
