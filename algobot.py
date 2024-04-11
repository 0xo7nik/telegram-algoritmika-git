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
def main(message):
    bot.send_message(message.from_user.id, "Привет, я бот математик. Могу помочь с любым математическим примером. Напиши, например, 2+2 и я тебе сразу отвечу")

@bot.message_handler(commands=["answer"])
def ans1(message):
    bot.send_message(message.from_user.id, "Напиши пример")

@bot.message_handler(content_types=['text'])
def ans2(message):
    num1 = message.text
    num2 = message.text
    if message.text == num1 and num2:
        bot.send_message(message.from_user.id, f"{num1}" + f"{num2}")

bot.polling(none_stop=True, interval=0, timeout=120)