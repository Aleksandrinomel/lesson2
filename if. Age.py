'''
1) Попросить пользователя ввести возраст при помощи input и положить результат в переменную
2) Написать функцию, которая по возрасту определит, чем должен заниматься пользователь: учиться в детском саду, школе, ВУЗе или работать
3) Вызвать функцию, передав ей возраст пользователя и положить результат работы функции в преременную
4) Вывести содержимое переменной на экран
'''


age = int(input("Введите ваш возраст: "))
act = 'Текущий род занятий: '


def activity(age):
    if age < 7:
        return act + 'учеба в детском саду.'
    elif 6 < age < 18:
        return act + 'учеба в школе.'
    elif 17 < age < 23:
        return act + 'учеба в ВУЗе.'
    elif 22 < age < 65:
        return act + 'работа.'
    else:
        return act + 'отдых на пенсии.'


activity = activity(age)
print(activity)
