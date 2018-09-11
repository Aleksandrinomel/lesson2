'''
1) Написать функцию, которая принимает на вход две строки
2) Проверить, является ли то что переданно функции строками. Если нет - вернуть 0
3) Если строки одинаковые, верунть 1
4) Если строки разные и первая длиннее, вернуть 2
5) Если строки разные и вторая строка 'learn', возвращает 3
6) Вызвать функцию несколько раз, передавая ей разные праметры и выводя на экран результаты
'''


def str_comparison(str1, str2):
    if type(str1) != type('') or type(str2) != type(''):
        return 0
    elif str1 == str2:
        return 1
    elif len(str1) > len(str2):
        return 2
    elif str1 != str2 and str2 == 'learn':
        return 3
print(str_comparison('Hi', 2))
print(str_comparison('Hi','Hi'))
print(str_comparison('Hi, Dude','Hi'))
print(str_comparison('Hi','learn'))

