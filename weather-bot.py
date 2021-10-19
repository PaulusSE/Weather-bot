import telebot
import sys
sys.path.append("C:/Program Files/Python38/Lib/site-packages")

import pyowm
from pyowm import OWM
from pyowm.utils import config
from pyowm.utils import timestamps
from pyowm.utils.config import get_default_config

bot = telebot.TeleBot("+++++++++++++++++++++++++++++")

config_dict = get_default_config()
config_dict['language'] = 'ru'
owm = OWM('4d2f71ad6a7b1aa51f14e6ca659b1825', config_dict)
mgr = owm.weather_manager()

@bot.message_handler(content_types=['text'])

def send_echo(message):

    observation = mgr.weather_at_place(message.text)
    w = observation.weather
    temp = w.temperature('celsius')["temp"]

    answer = "Сейчас в городе " + message.text + ' ' + w.detailed_status + '\n'
    answer += 'Температура в районе ' + str(temp) + '°C\n\n'

    if temp < 10:
        answer += ("Не забудь подштанники!")
    elif temp < 20:
        answer += ('Норм погода, можно в футболке и в кофте')
    else:
        answer += ("Шорты - лучший выбор")
    answer += '\n\n' + str(w)
    #bot.reply_to(message, message.text)
    bot.send_message(message.chat.id, answer)

bot.polling( none_stop = True )
