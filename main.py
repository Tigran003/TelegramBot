import telebot
import webbrowser
from telebot import types
from telebot.types import Update
from cofig import bot
from money_change import change, summa, callback
from registration import registration, user_name, user_pass



@bot.message_handler(commands=['site','website'])
def site(message):
    webbrowser.open(('https://www.instagram.com/'))


@bot.message_handler(commands=['search''💁'])
def main(message):
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton('Search anything you want 🧐', url='https://www.mobilecentre.am/')
    markup.row(btn1)
    btn2 = types.InlineKeyboardButton(text='Top free apps for windows 💣', url='https://www.microsoft.com/en-US/store/top-free/apps/pc')
    btn3 = types.InlineKeyboardButton(text='Top free apps for Android 💣', url='https://techpp.com/2021/08/03/best-free-android-apps/')
    markup.row(btn2,btn3)
    bot.reply_to(message, 'search',reply_markup=markup)


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('/search''💁')
    btn2 = types.KeyboardButton('/help''🛠️')
    btn3 = types.KeyboardButton('/registration''📝')
    btn4 = types.KeyboardButton('/change''💱')
    markup.row(btn1, btn2)
    markup.row(btn3,btn4)
    bot.send_message(message.chat.id,f'Hello,{message.from_user.first_name} {message.from_user.last_name}', reply_markup=markup)
    bot.register_next_step_handler(message)


@bot.message_handler(commands=['help''🛠️'])
def main(message):
    bot.send_message(message.chat.id, '<b>Help</b> <em><u>information</u></em>', parse_mode='html')


@bot.message_handler()
def info(message):
    if message.text.lower() == 'hello':
        bot.send_message(message.chat.id,f'Hello,{message.from_user.first_name} {message.from_user.last_name}' )
    elif message.text.lower() == 'id':
        bot.reply_to(message, f'ID: {message.from_user.id}')


@bot.message_handler(content_types=['photo'])
def get_photos(message):
    bot.reply_to(message,'So beautifull photo!')





bot.infinity_polling()

