import json
import requests
import telebot
from ini import *
bot = telebot.TeleBot(TOKEN)

class ConvertionException(Exception):
    pass

class CryptoCoverter:
    @staticmethod
    def conv(message: telebot.types.Message, tmp):
        try:
            tmp = tmp.split(' ')
            if len(tmp) != 3:
                raise ConvertionException('Введено больше символов чем необходимо!\nПопробуем еще раз...')
            src, ext, qnty = tmp

            if src == ext:
                raise ConvertionException(f'Непонятно зачем переводить {src} в {ext}?\nОни же одинаковые!\nЭто же перевес пороток на другой гвоздок!')

            if src not in keys.keys() or ext not in keys.keys():
                raise ConvertionException('очепятка! внимательнее, пожалуйста!\nпопробуем еще раз...')

            try:
                qnty = float(qnty)
            except ValueError:
                raise ConvertionException(f'не понял - {qnty}, скока надо!\nпопробуем еще раз...')

        except ConvertionException as e:
            bot.reply_to(message, f'упс...\n{e}')
        except Exception as e:
            bot.reply_to(message, f'упс...\n{e}')
        else:
            r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={keys[src]}&tsyms={keys[ext]}')
            total = json.loads(r.content)[keys[ext]] * qnty
            return (f'цена за {qnty} {src} в {ext}ах будет {total}')