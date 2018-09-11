'''
1) Напишите функцию ask_user(), которая с помощью input() спрашивает пользователя “Как дела?”, пока он не ответит “Хорошо”
2) Создайте словарь типа "вопрос": "ответ", например: {"Как дела": "Хорошо!", "Что делаешь?": "Программирую"} и так далее
3) Доработайте ask_user() так, чтобы когда пользователь вводил вопрос который есть в словаре, программа давала ему соотвествующий ответ.
'''


def ask_user():
    questionnaire = {'Как дела?': '', 'Что делаешь?': '', 'Кто ты?': '', 'Сколько тебе лет?': ''}

    # заполняем словарь, где вопрос-ключ известен, а ответ-значение - пользовательский ввод.
    for key in questionnaire.keys():
        if key == 'Как дела?':
            while True:
                answer = input('Как дела?')
                if answer == 'Хорошо':
                    print('У тебя не было выбора, Ха-Ха')
                    questionnaire['Как дела?'] = answer
                    break
                else:
                    print(answer, '?', ' Так не пойдет... Попробуй еще раз!')
        else:
            questionnaire[key] = input(key)
    print(questionnaire)

    # Пишем вопрос-ключ, получаем ответ-значение.
    while True:
        ask = input('Задайте вопрос: ')
        if ask == 'Как это остановить?':
            print('Я тебя понял. Пока!')
            break
        else:
            if ask in questionnaire.keys():
                print('Ответчик:', questionnaire[ask])
            else:
                print('Ответ отсутствует! Попробуйте другой вопрос')


ask_user()