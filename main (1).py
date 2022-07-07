from time import time, sleep
from selenium import webdriver
from datetime import datetime
import telebot
import random
from main import posolstvo as p

bot = telebot.TeleBot('5172625256:AAFiNGBCNovkjg1EeOs1XMuL-v4R2udtoXU')

PATH = r"C:\chromedriver.exe"


url = 'https://pieraksts.mfa.gov.lv/ru/moskva'

def rnd():
    return random.randint(1, 2)

@bot.message_handler(commands=['start', 'help'])
def checker(m):
    bot.send_message(m.chat.id, 'Я буду смотреть посольство раз в 1-2 минуты')
    while True:
        try:
            r = rnd()
            bot.send_message(m.from_user.id, f'в следующий раз посмотрю через {r} минут')
            sleep(r * 60)
            msg, tm, dt = p()
            if msg == 'Šobrīd visi pieejamie laiki ir aizņemti':
                bot.send_message(m.from_user.id, (f'пока тихо {dt}'))
            else:
                bot.send_message(m.from_user.id, f'записал тебя на {tm} ,нез {dt}')
        except:
            sleep(60)
            bot.send_message(m.from_user.id, 'что-то не так, смотрю еще раз')
            try: msg, time, dt = p()
            except:
                bot.send_message(m.from_user.id, 'проверил и словил какую-то ошибку')



@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.from_user.id, 'Привет\nЩа посмотрю, что там по записям...')
        try:
            msg, time, dt = p()
            if msg == 'Šobrīd visi pieejamie laiki ir aizņemti':
                bot.send_message(message.from_user.id, (f'пока тихо {dt}'))
            else:
                bot.send_message(message.from_user.id, f'записал на {time}, {dt}')
        except:
            sleep(60)
            bot.send_message(message.from_user.id, 'что-то не так, смотрю еще раз')
            try: msg, time, dt = p()
            except:
                bot.send_message(message.from_user.id, 'проверил и словил какую-то ошибку')



    else:
        bot.send_message(message.from_user.id, "Entschuldingung?")













while True:
    try:
        bot.polling(non_stop=True, interval=0)
    except:
        pass

