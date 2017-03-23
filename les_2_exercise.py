from datetime import datetime, date, timedelta
import locale
dt_now = datetime.now()
dt2 = datetime(2015, 5, 16, 8, 3, 44)
print(dt2)
print(dt_now - dt2)

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
