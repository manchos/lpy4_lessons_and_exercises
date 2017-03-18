from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

def greet_user(bot, update):
    print('Вызван /start')
    bot.sendMessage(update.message.chat_id, text='Давай общаться!')

def show_error(bot, update, error):
    print(error)

def talk_to_me(bot, update):
    print(update.message.text)
    bot.sendMessage(update.message.chat_id, update.message.text)

def main():
    updater = Updater("API_KEY")

    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(MessageHandler([Filters.text], talk_to_me))

    dp.add_error_handler(show_error)

    updater.start_polling()
    updater.idle()


main()
