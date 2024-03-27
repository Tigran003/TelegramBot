from telebot import types

from cofig import bot
from currency_converter import CurrencyConverter

import requests

# currency = CurrencyConverter()

url = 'https://cdn.jsdelivr.net/npm/@fawazahmed0/currency-api@latest/v1/currencies/'

amount = 0


@bot.message_handler(commands=['change''💱'])
def change(message):
    bot.send_message(message.chat.id,'Hello,Enter the mount')
    bot.register_next_step_handler(message,summa)


def summa(message):
    global amount
    try:
        amount = int(message.text.strip())
    except ValueError:
        bot.send_message(message.chat.id,'Wrong format!! Write amount!')
        bot.register_next_step_handler(message,summa)
        return
    if amount > 0:
        markup = types.InlineKeyboardMarkup(row_width=2)
        btn1 = types.InlineKeyboardButton('USD/BTC', callback_data='usd/btc')
        btn2 = types.InlineKeyboardButton('BTC/USD', callback_data='btc/usd')
        btn3 = types.InlineKeyboardButton('USD/AMD', callback_data='usd/amd')
        btn4 = types.InlineKeyboardButton('AMD/USD', callback_data='amd/usd')
        btn5 = types.InlineKeyboardButton('AMD/BTC', callback_data='amd/btc')
        btn6 = types.InlineKeyboardButton('AMD/RUB', callback_data='amd/rub')
        btn7 = types.InlineKeyboardButton('RUB/AMD', callback_data='rub/amd')
        markup.add(btn1, btn2, btn3, btn4,btn5,btn6,btn7)
        bot.send_message(message.chat.id,'Select a currency pair',reply_markup=markup)
    else:
        bot.send_message(message.chat.id,'Amount must be greater 0!Enter amount')
        bot.register_next_step_handler(message,summa)




@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    values = call.data.lower().split('/')
    # res = currency.convert(amount, values[0], values[1])
    data = requests.get(url + values[0] + '.json').json().get(values[0])
    res = data.get(values[1]) * amount
    # to = requests.get(url + values[1] + 'json/')
    bot.send_message(call.message.chat.id, f'Its turns out: {round(res, 2)}. You can enter new amount')
    bot.register_next_step_handler(call.message, summa)


