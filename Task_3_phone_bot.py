import telebot

token = '5434161555:AAGJZZIBqLG1hbayH2aQmgBWSO_gwzKsIr8'

bot = telebot.TeleBot(token)


@bot.message_handler(commands=['help'])
def start(msg: telebot.types.Message):
    bot.send_message(chat_id=msg.from_user.id,
                     text=f'Привет, {msg.from_user.first_name}, вот список команд для работы:\n/view - просмотр справочника\n/add "Фамилия, Имя, номер телефона, описание" - добавить запись\n/find "строка для поиска" - найти запись\n/delete "строка для удаления"- удалить запись\n/export "имя_файла.txt"- экспорт в .txt\n/import "имя_файла.txt"- импорт из .txt')


@bot.message_handler(commands=['view'])
def view(msg: telebot.types.Message):
    bot.send_message(chat_id=msg.from_user.id,
                     text=f'Просмотр записей')
    file = 'base.txt'
    with open(file, 'r', encoding="utf-8") as data:
        for line in data:
            bot.send_message(chat_id=msg.from_user.id,
                             text=line)


@bot.message_handler(commands=['add'])
def add(msg: telebot.types.Message):
    bot.send_message(chat_id=msg.from_user.id,
                     text=f'Добавление записи')
    file = 'base.txt'
    a = msg.text.replace('/add','')
    with open(file, 'a', encoding="utf-8") as data:
        data.write('\n'+ a +'\n')
        bot.send_message(chat_id=msg.from_user.id,text=f'Добавлено {a}')


@bot.message_handler(commands=['find'])
def find(msg: telebot.types.Message):
    s = msg.text.replace('/find','')
    bot.send_message(chat_id=msg.from_user.id,text=s)
    with open('base.txt', 'r', encoding="utf-8") as data:
        for line in data:
            if s in line:
                bot.send_message(chat_id=msg.from_user.id,text=line)


@bot.message_handler(commands=['delete'])
def delete(msg: telebot.types.Message):
    bot.send_message(chat_id=msg.from_user.id,
                     text=f'Будет реализовано в следующих версиях :(')


@bot.message_handler(commands=['import'])
def importtxt(msg: telebot.types.Message):
    s = msg.text.replace('/import','')
    data_import = open(s, 'r', encoding="utf-8")
    data = open('base.txt', 'a', encoding="utf-8")
    data.writelines('\n')
    for line in data_import:
            data.writelines(line)
    bot.send_message(chat_id=msg.from_user.id,
                     text=f'Импорт завершен')
    data.close()
    data_import.close()


@bot.message_handler(commands=['export'])
def exporttxt(msg: telebot.types.Message):
    s = msg.text.replace('/export','')
    data_export = open(s, 'w', encoding="utf-8")
    data = open('base.txt', 'r', encoding="utf-8")
    for line in data:
        items = (line)
        data_export.writelines(items)
    data.close()
    data_export.close()
    bot.send_message(chat_id=msg.from_user.id,
                     text=f'Готово, ловите файл... ')
    bot.send_document(chat_id=msg.from_user.id, document= open(s,'rb'))
    


@bot.message_handler()
def phones(msg: telebot.types.Message):
    bot.send_message(chat_id=msg.from_user.id,
                     text=f'Введите /help для просмотра доступных команд')


print('Server start...')
bot.polling()
