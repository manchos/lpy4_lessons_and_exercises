from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import re
import schedule
import time

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
        expr = in_quotes.group(1).strip()
        if expr[-1] == '=': # последний знак в выражении должен быть =
            try:
                m2 = re.search(r'(\s*(\d+\s*[+-\\*\\/]\s*\d+\s*)=)', expr)
                print(m2.group(2))
                bot_response = eval(m2.group(2))
            except (AttributeError):
                bot_response = "Лажа. Введи выражение правильно"
            except (ZeroDivisionError):
                bot_response = "На ноль делить!!!???"
        else:
            bot_response = "Лажа. В конце выражения должен стоять знак '='"
    except (AttributeError):
        bot_response = update.message.text
        pass
    bot.sendMessage(update.message.chat_id, bot_response)




# def shedule_message(bot, update):
#     schedule.every(1).minutes.do(bot.sendMessage(update.message.chat_id, text='Давай общаться!'))
#
#
# def callback_minute(bot, job):
#     bot.send_message(job.context, text='One message every minute')



def callback_alarm(bot, job):
    print('callback_alarm')
    bot.send_message(chat_id=job.context, text='BEEP')


def callback_timer(bot, update, job_queue):
    print('callback_timer')
    bot.send_message(chat_id=update.message.chat_id, text='Setting a timer for 1 minute!')
    job_queue.run_repeating(callback_alarm, 20, context=update.message.chat_id)

#

def callback_30(bot, job):
    bot.send_message(chat_id='@manchos_bot', text='A single message with 30s delay')

def main():
    updater = Updater("379170475:AAGMcg2qYxJwEUI9WkiUIkz-yD1UmfUESYI")

    # j = updater.job_queue
    #
    # j.run_once(callback_30, 30, context=update.message.chat_id)


    dp = updater.dispatcher
    dp.add_handler(CommandHandler('stench', callback_timer, pass_job_queue=True))
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("wordcount", words_count))

    dp.add_handler(CommandHandler("wordcount", words_count))

    # dp.add_handler(MessageHandler([Filters.text], talk_to_me))

    dp.add_error_handler(show_error)






    updater.start_polling()
    updater.idle()


main()
