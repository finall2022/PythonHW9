import telebot
import datetime

bot = telebot.TeleBot('5434161555:AAGJZZIBqLG1hbayH2aQmgBWSO_gwzKsIr8')

buttons = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
buttons_act = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
buttons.row(telebot.types.KeyboardButton('Комплексные'),
            telebot.types.KeyboardButton('Рациональные'),
            telebot.types.KeyboardButton('Ещё не определился'))

buttons_act.row(telebot.types.KeyboardButton('+'),
                telebot.types.KeyboardButton('-'),
                telebot.types.KeyboardButton('*'),
                telebot.types.KeyboardButton('/'))

global now
now = datetime.datetime.now()


@bot.message_handler()
def hello(msg: telebot.types.Message):
    bot.send_message(chat_id=msg.from_user.id,
                     text='Здравствуйте.\nВыберите режим работы калькулятора.',
                     reply_markup=buttons)
    bot.register_next_step_handler(msg, answer)


def answer(msg: telebot.types.Message):
    if msg.text == 'Комплексные':
        bot.register_next_step_handler(msg, complex_counter1)
        bot.send_message(chat_id=msg.from_user.id, text='Введите первое комплексное число.',
                         reply_markup=telebot.types.ReplyKeyboardRemove())
        logging(f'{now} Выбран режим комплексных чисел;')
    elif msg.text == 'Рациональные':
        bot.register_next_step_handler(msg, rational_counter)
        bot.send_message(chat_id=msg.from_user.id, text='Введите выражение с рациональными числами.',
                         reply_markup=telebot.types.ReplyKeyboardRemove())
        logging(f'{now} Выбран режим рациональных чисел; ')
    elif msg.text == 'Ещё не определился':
        bot.register_next_step_handler(msg, answer)
        bot.send_message(chat_id=msg.from_user.id,
                         text='Возвращайтесь, когда определитесь.')
        logging(f'{now} Отказ от ввода;\n')
    else:
        bot.register_next_step_handler(msg, answer)
        bot.send_message(chat_id=msg.from_user.id,
                         text='Пожалуйста, используйте кнопки.')
        logging(f'{now} Ошибка ввода;\n')

        bot.send_message(chat_id=msg.from_user.id,
                         text='Выберите режим работы калькулятора.', reply_markup=buttons)


def complex_counter1(msg: telebot.types.Message):
    bot.register_next_step_handler(msg, complex_counter2)

    bot.send_message(chat_id=msg.from_user.id, text='Выберите действие',
                     reply_markup=buttons_act)
    global aa
    aa = msg.text.replace(' ', '')
    logging('Введено ' + aa + ';')


def complex_counter2(msg: telebot.types.Message):
    bot.register_next_step_handler(msg, complex_result)
    bot.send_message(chat_id=msg.from_user.id, text='Введите второе число')
    global act
    act = msg.text
    logging('Выбрано действие: ' + act + ';')


def complex_result(msg: telebot.types.Message):

    bot.send_message(chat_id=msg.from_user.id, text=f'Результат:',
                     reply_markup=telebot.types.ReplyKeyboardRemove())
    global bb
    bb = msg.text.replace(' ', '')
    logging('Введено ' + bb + ';')

    a = 0
    if act == '+':
        a = (complex(aa) + complex(bb))
        bot.send_message(chat_id=msg.from_user.id, text=a,
                         reply_markup=telebot.types.ReplyKeyboardRemove())
    elif act == '-':
        a = (complex(aa) - complex(bb))
        bot.send_message(chat_id=msg.from_user.id, text=(
            complex(aa) - complex(bb)), reply_markup=telebot.types.ReplyKeyboardRemove())
    elif act == '*':
        a = (complex(aa) * complex(bb))
        bot.send_message(chat_id=msg.from_user.id, text=(
            complex(aa) * complex(bb)), reply_markup=telebot.types.ReplyKeyboardRemove())
    elif act == '/':
        a = (complex(aa) - complex(bb))
        bot.send_message(chat_id=msg.from_user.id, text=(
            complex(aa) / complex(bb)), reply_markup=telebot.types.ReplyKeyboardRemove())

    logging(f'Получен ответ: {a} \n')
    bot.register_next_step_handler(msg, hello)


def rational_counter(msg: telebot.types.Message):

    c = msg.text.replace(' ', '')
    logging('Введено ' + c)
    s = 0
    if '+' in c:
        c = msg.text.split('+')
        a1 = float(c[0])
        a2 = float(c[1])
        s = a1 + a2
    elif '-' in c:
        c = msg.text.split('-')
        a1 = float(c[0])
        a2 = float(c[1])
        s = a1 - a2
    elif '*' in c:
        c = msg.text.split('*')
        a1 = float(c[0])
        a2 = float(c[1])
        s = a1 * a2
    elif '/' in c:
        c = msg.text.split('/')
        a1 = float(c[0])
        a2 = float(c[1])
        s = a1 / a2

    bot.send_message(chat_id=msg.from_user.id, text=f'{msg.text} = {s}')
    logging(f'Получен ответ: {s} \n')


def logging(line):
    with open('action.log', 'a', encoding="utf-8") as data:
        data.write(line + ' ')


print('Server start...')
bot.polling()
