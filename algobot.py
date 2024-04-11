import telebot
import json

def get_token():
    token = ''
    with open('token.json') as file:
        json_answer = json.load(file)
        token = json_answer['config']
    return token

token = get_token()
bot = telebot.TeleBot(token)

@bot.message_handler(commands=["start"])
def send_start(message):
    if message.text.lower() == "/start":
        bot.send_message(message.from_user.id, "Привет, я бот математик. Могу помочь с любым математическим примером. Напиши, например, 2+2 и я тебе сразу отвечу")

@bot.message_handler(commands=["answer"])
def ans1(message):
    bot.send_message(message.from_user.id, "Напиши пример")

@bot.message_handler(content_types=['text'])
def ans2(message):
    num1 = message.interval
    num2 = message.interval
    if message.text == num1 and num2:
        bot.send_message(message.from_user.id, message.send_message)
    print(message)

bot.polling(none_stop=True, interval=0, timeout=120)