# 2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя: имя,
# фамилия, год рождения, город проживания, email, телефон. Функция должна принимать параметры как
# именованные аргументы. Реализовать вывод данных о пользователе одной строкой.

def my_func(name, surname, birthday, city, email, phonenumber):
    return [name, surname, birthday, city, email, phonenumber]


print(my_func(name='Richard', surname='Branson', birthday='18.07.1950', city='London', email='rb@virgin.uk',
              phonenumber='+14351353135'))
