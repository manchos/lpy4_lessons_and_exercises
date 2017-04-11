from datetime import datetime, date, timedelta
import locale
import re
import csv
import sys



dt_now = datetime.now()
dt2 = datetime(2015, 5, 16, 8, 3, 44)
print(dt2)
print(dt_now - dt2)

print(sys.platform)

if sys.platform == 'win32':
    locale.setlocale(locale.LC_ALL, 'rus_rus')
else:
    locale.setlocale(locale.LC_ALL, 'ru_RU.UTF-8')

print(dt_now.strftime('%B'))

print('============================timedelta=========================================')

# Использование timedelta
dt = date(2000, 1, 1)
delta = timedelta(days=1)
print(delta)
print(dt - delta)
print(dt + delta)

print('=============================strftime========================================')

# Вывод даты на экран
print(dt_now.strftime('%d.%m.%Y %H:%M'))
print(dt_now.strftime('%A %d %B %Y'))

# print(locale.setlocale(locale.LC_TIME, "ru_RU"))
print(dt_now.strftime('%A %d %B %Y'))

# Получение даты из строки
date_string = '12/23/2010'
date_dt = datetime.strptime(date_string, '%m/%d/%Y')
print(date_dt)

print('=============================Задание по датам========================================')
"""
Задание
Напечатайте в консоль даты: вчера, сегодня, месяц назад
Превратите строку "01/01/17 12:10:03.234567" в объект datetime
"""
print('Вчера : %s' % (datetime.now() - delta).strftime('%d.%m.%Y'))
print('Сегодня : %s' % datetime.now().strftime('%d.%m.%Y'))
print('Месяц назад : %s' % (datetime.now() - timedelta(days=30)).strftime('%d.%m.%Y'))

date_string_1 = "01/01/17 12:10:03.234567"
print(datetime.strptime(date_string_1, '%m/%d/%y %H:%M:%S.%f'))

print('=============================Задание по работе с файлами========================================')
"""
Задание
Скачайте файл по ссылке https://www.dropbox.com/s/sipsmqpw1gwzd37/referat.txt?dl=0
Прочитайте его и подсчитайте количество слов в тексте
"""
with open('files/referat.txt', 'r', encoding='utf-8') as f:
    content = f.read()
found = re.findall(r'\S+\b', content)
print('количество слов в тексте: %s' % len(found))

print('=============================Задание по работе с CSV========================================')

"""
Задание
Возьмите словарь с ответами из функции get_answer
Запишите его содержимое в формате csv в формате: "ключ"; "значение". Каждая пара ключ-значение должна располагаться на отдельной строке
"""

answers = {
    "привет": "Привет!",
    "как дела": "Отлично, а у тебя?",
    "Пока!": "Еще увидимся!",
    "Хорошо": "Молодца!"
}

with open('files/export.csv', 'w', encoding='utf-8') as f:
    fields = ['ключ', 'значение']
    writer = csv.DictWriter(f, fields, delimiter=';')
    writer.writeheader()
    for key, value in answers.items():
        # print(key, value)
        writer.writerow({'ключ': key, 'значение': value})

with open('files/export.csv', 'r', encoding='utf-8') as f:
    content = f.read()
print(content)