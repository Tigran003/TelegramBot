import sqlite3
from cofig import bot

name = None

@bot.message_handler(commands=['registration''📝'])
def registration(message):
    conn = sqlite3.connect('mybase.sql')
    cur = conn.cursor()

    cur.execute('CREATE TABLE IF NOT EXISTS users (id int auto_increment primary key, name varchar(50), pass varchar(50))')
    conn.commit()
    cur.close()
    conn.close()

    bot.send_message(message.chat.id, 'Hello,Lets register you!Please enter your name ')
    bot.register_next_step_handler(message,user_name)

def user_name(message):
    global name
    name = message.text.strip()
    bot.send_message(message.chat.id, 'Enter password! ')
    bot.register_next_step_handler(message, user_pass)


def user_pass(message):
    password = message.text.strip()

    conn = sqlite3.connect('mybase.sql')
    cur = conn.cursor()

    cur.execute(f"INSERT INTO users (name, pass) VALUES ('%s', '%s')" % (name, password))
    conn.commit()
    cur.close()
    conn.close()


    bot.send_message(message.chat.id, 'You registered successfully! ')