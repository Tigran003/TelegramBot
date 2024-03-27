# import requests
# from cofig import bot
# from cofig import API
#
# @bot.message_handler(commands=['weather'])
# def weather(message):
#     bot.send_message(message.chat.id,'Hello!,nice to see you, write country or city name ')
#
#
# @bot.message_handler(content_types=['text'])
# def get_weather(message):
#     city = message.text
#     res = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API}&units=metric')
#     bot.reply_to(message,f'weather now: {res.json()}')


