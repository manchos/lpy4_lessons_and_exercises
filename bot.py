from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import re

def greet_user(bot, update):
    print('Вызван /start')
    bot.sendMessage(update.message.chat_id, text='Давай общаться!')

def words_count(bot, update):
    print('Вызван /wordcount')
    # count = len(update.message.text.split(''))
    bot_text = re.search(r'"(.*)"', update.message.text) #есть ли что-то в ковычках

    if bot_text.group(1):
        bot_text = re.sub(r'\s+', ' ', bot_text.group(1)).strip() # удаляем пробелы
        count = len(bot_text.split(' '))
        bot.sendMessage(update.message.chat_id, text='{} слова'.format(count))

def show_error(bot, update, error):
    print(error)

def talk_to_me(bot, update):
    print(update.message.text)
    try:
        in_quotes = re.search(r'"(.*)"', update.message.text)
        if in_quotes.group(1)[-1] == '=':
            try:
                m2 = re.search(r'"(\s*(\d+\s*[+-\\*\\/]\s*\d+\s*)=)"', update.message.text)
                print(m2.group(2))
                bot_response = eval(m2.group(2))
            except (AttributeError):
                bot_response = "Лажа. Введи выражение правильно"
            except (ZeroDivisionError):
                bot_response = "На ноль делить!!!???"
    except (AttributeError):
        bot_response = update.message.text
    bot.sendMessage(update.message.chat_id, bot_response)

def main():
    updater = Updater("379170475:AAGMcg2qYxJwEUI9WkiUIkz-yD1UmfUESYI")

    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("wordcount", words_count))

    dp.add_handler(MessageHandler([Filters.text], talk_to_me))

    dp.add_error_handler(show_error)

    updater.start_polling()
    updater.idle()


main()
