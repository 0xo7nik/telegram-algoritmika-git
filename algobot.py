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

@bot.message_handler(commands=["start", "help"])
def send_start(message):
    if message.text.lower() == "/start":
        bot.send_message(message.from_user.id, "Привет! Я могу помочь тебе с любым математическим выражением.")
    if message.text.lower() == "/help":
        bot.send_message(message.from_user.id, "Напиши выражение, которое надо решить")

@bot.message_handler(content_types=['text'])
def send_answer(message):
    if message.text.lower():
        bot.send_message(message.from_user.id, "1")

bot.polling(none_stop=True, interval=0, timeout=120)


@bot.message_handler(func=lambda message: True)
def calc(message): 
#    try: 
#        result = parser.parse(message.text)
#        bot.send_message(message.chat.id, str(result)) 
#    except:
    pass