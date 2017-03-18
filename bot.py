from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

def greet_user(bot, update):
    print('Вызван /start')
    bot.sendMessage(update.message.chat_id, text='Давай общаться!')

def words_count(bot, update):
    print('Вызван /wordcount')
    # count = len(update.message.text.split(''))
    bot_text = update.message.text.split(' ')
    count = len(bot_text[1].split(" "))

    bot.sendMessage(update.message.chat_id, text=count)


def show_error(bot, update, error):
    print(error)

def talk_to_me(bot, update):
    print(update.message.text)
    bot.sendMessage(update.message.chat_id, update.message.text)

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
