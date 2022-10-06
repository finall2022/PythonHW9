import telebot


token = '5434161555:AAGJZZIBqLG1hbayH2aQmgBWSO_gwzKsIr8'

bot = telebot.TeleBot(token)


@bot.message_handler(commands=['hello'])
def hello_answer(msg: telebot.types.Message):
    bot.send_message(chat_id=msg.from_user.id,
                     text=f'Привет, {msg.from_user.first_name}')


@bot.message_handler()
def answer(msg: telebot.types.Message):
    bot.send_message(chat_id=msg.from_user.id,
                     text=f'Не вводите буквы - бот ломается :)')
    while not msg.text.isdigit():
        bot.send_message(chat_id=msg.from_user.id,
                         text=f'Введите числа в формате A + B (с пробелами)')
        break
    if ' ' not in msg.text:
        bot.send_message(chat_id=msg.from_user.id,
                         text=f'Введите пример в формате A + B (с пробелами)')
    else:
        c = msg.text.split(' ')
        if '+' in c:
            a1 = float(c[0])
            a2 = float(c[2])
            s = summ(a1, a2)
        elif '-' in c:
            a1 = float(c[0])
            a2 = float(c[2])
            s = diff(a1, a2)
        elif '*' in c:
            a1 = float(c[0])
            a2 = float(c[2])
            s = mult(a1, a2)
        elif '/' in c:
            a1 = float(c[0])
            a2 = float(c[2])
            s = div(a1, a2)

        bot.send_message(chat_id=msg.from_user.id,
                         text=f'{msg.text} = {s}')


def summ(a, b):
    return a+b


def diff(a, b):
    return a-b


def mult(a, b):
    return a*b


def div(a, b):
    return a/b


print('Server start...')
bot.polling()
