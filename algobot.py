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
    bot.send_message(message.from_user.id, "Тут пока ничего нет, но есть мои контакты: https://t.me/sitectov \nhttps://github.com/0xo7nik \nhttps://vk.com/sitect")

bot.polling(none_stop=True, interval=0, timeout=120)