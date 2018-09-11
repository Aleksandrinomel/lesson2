'''Перепишите функцию ask_user() из задания про while, чтобы она перехватывала KeyboardInterrupt,
писала пользователю "Пока!" и завершала работу при помощи оператора break'''

questionnaire = {'Как дела?': 'Хорошо', 'Что делаешь?': 'Кожу', 'Кто ты?': 'Я', 'Сколько тебе лет?': '23'}


def ask_user():
    while True:
        try:
            ask = input('Задайте вопрос: ')
            if ask == 'Как это остановить?':
                print('Я тебя понял. Пока!')
                break
            else:
                if ask in questionnaire.keys():
                    print('Ответчик:', questionnaire[ask])
                else:
                    print('Ответ отсутствует! Попробуйте другой вопрос')
        except KeyboardInterrupt:
            print('Пока!')
            break


ask_user()