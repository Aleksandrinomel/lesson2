'''
1) Установите модуль ephem
2) Добавьте в бота команду /planet, которая будет принимать на вход название планеты на английском, например /ephem Mars
3) В функции-обработчике команды из update.message.text получите название планеты (подсказка: используйте .split())
4) При помощи условного оператора if и ephem.constellation научите бота отвечать, в каком созвездии сегодня находится планета.
'''

import datetime
from telegram.ext import Updater, CommandHandler
import settings
import ephem


# обрабатывает команду бота /planet и выводит созвездие, в котором сейчас находится планета
def greet_user(bot, update):
    if update.message.text.split()[0] == '/planet':
        now = datetime.datetime.now()
        planet_is = 'ephem.' + update.message.text.split()[1] + "('" + str(now) + "')"
        constell = ephem.constellation(eval(planet_is))
        update.message.reply_text('Планета ' + update.message.text.split()[1] + ' сейчас находится в созвездии ' + constell[1])


def main():
    mybot = Updater(settings.API_KEY, request_kwargs=settings.PROXY)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler('planet', greet_user))

    mybot.start_polling()
    mybot.idle()


main()
