import telebot
import json
import math
import types

def get_token():
    token = ''
    with open('token.json') as file:
        json_answer = json.load(file)
        token = json_answer['config']
    return token

token = get_token()
bot = telebot.TeleBot(token)

#@bot.message_handler(commands=["start"])
#def main(message):
#    bot.send_message(message.from_user.id, "Привет, чем могу помочь?")

# keybord
markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
item1 = types.KeyboardButton('ТЫ ГЕЙ??!!')
item2 = types.KeyboardButton('Ну ты же гей?')

markup.add(item1, item2)
@bot.message_handler(content_types=['text'])
def main(message):
    bot.send_message(message.chat.id, 'Дарова, {0.first_name}!\
                    parse_made=html, reply_markup=markup')


#@bot.message_handler(commands=["start"])
#def main(message):
#    bot.send_message(message.from_user.id, "Привет, я бот математик. Могу помочь с любым математическим примером. Напиши, например, 2+2 и я тебе сразу отвечу.")

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.chat.type == 'привет':
        if message.text == 'ТЫ ГЕЙ??!!':
            bot.send_message(message.chat.id, 'Нет это ты')
        elif message.text == 'Ну ты жу гей?':
            bot.send_message(message.chat.id, 'опять же это ты')
        else:
            bot.send_message(message.chat.id, 'ди нах')
#    if message.text.lower() == "привет":
#        bot.send_message(message.from_user.id, "QQ")
#    elif message.text == "/help":
#        bot.send_message(message.from_user.id, "Напиши привет")
#    else:
#        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")
markup.add(item1, item2)

bot.polling(none_stop=True, interval=0, timeout=120)