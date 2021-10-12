import telebot
from cls import *

@bot.message_handler(commands=['help','start'])
def help(message: telebot.types.Message):
    text='для начала работы бота необходимо ввести команду в следующем формате:\n' \
         '<какую монету меняем> <монета на которую меняем> <количество>\n' \
         'для получения списка моент введите команду /values'
    bot.reply_to(message, text)

@bot.message_handler(commands=['values'])
def coin(message: telebot.types.Message):
    text = 'Доступные монеты: '
    for k in keys.keys():
        text = '\n'.join((text, k,))
    bot.reply_to(message, text)

@bot.message_handler(content_types=['text'])
def stock(message: telebot.types.Message):
    text = CryptoCoverter.conv(message, message.text)
    bot.send_message(message.chat.id, text)

bot.polling(none_stop=True, interval=2)
