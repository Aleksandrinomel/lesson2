'''
1) Напишите функцию get_summ(num_one, num_two), которая принимает на вход два целых числа (int) и складывает их
2) Оба аргумента нужно приводить к целому числу при помощи int()
 и перехватывать исключение ValueError если приведение типов не сработало
 '''


def get_summ(num_one, num_two):
    try:
        return int(num_one) + int(num_two)
    except ValueError:
        return 'Nope'


num_one = 7
num_two = '7'
print(get_summ(num_one, num_two))
