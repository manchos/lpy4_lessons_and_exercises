# -*- coding: utf-8 -*-
import ftplib
import os
import socket
import sys
from datetime import datetime, date, timedelta
import locale
import shutil
import re
import encodings.idna
from myhosts import user, passwd, HOST, LOCALHOST


# DIRN = '/Электронный архив'

if sys.platform == 'win32':
    locale.setlocale(locale.LC_ALL, 'rus_rus')
else:
    locale.setlocale(locale.LC_ALL, 'ru_RU.UTF-8')


dt_now = datetime.now()
delta = timedelta(days=1)
dt_now = dt_now - delta

print(dt_now.strftime('%B'))
print(dt_now.strftime('%Y'))
DIR_analiz_reag = '/Электронный архив/#РОССИЯ/6.ЦФО/#Материалы_для_ежедневного_селекторного_совещания/' + dt_now.strftime('%Y') \
       + '/' + dt_now.strftime('%m') + '. ' + dt_now.strftime('%B') + ' ' + dt_now.strftime('%Y') + '/' + \
       dt_now.strftime('%d.%m.%Y') + '/Анализ реагирования'
DIR_mos_obl = DIR_analiz_reag + '/Московская область'

dir_local = '\\\\'+LOCALHOST+'\\cmp_data\Оперативный дежурный\\!_левая машина\\1_ОПЕРАТИВНЫЙ ДЕЖУРНЫЙ\\Планируемые сжигания порубочных остатков от МО'


dir_local_y = os.path.join(dir_local, dt_now.strftime('%Y'))
if os.path.exists(dir_local_y):
    print('КРУТЯК')
else:
    os.mkdir(dir_local_y)
    print('создана папка %s' % dt_now.strftime('%Y'))

dir_local_y_m = os.path.join(dir_local_y, dt_now.strftime('%B'))
if os.path.exists(dir_local_y_m):
    print('СУПЕРКРУТЯК')
else:
    os.mkdir(dir_local_y_m)
    print('создана папка %s' % dt_now.strftime('%B'))

dir_local_y_m_d = os.path.join(dir_local_y_m, dt_now.strftime('%d.%m.%Y'))
if os.path.exists(dir_local_y_m_d):
    print(dir_local_y_m_d)
else:
    os.mkdir(dir_local_y_m_d)
    print('создана папка %s' % dt_now.strftime('%B'))

print(sys.getdefaultencoding())
print(sys.getfilesystemencoding())



# print(f.__class__.encoding = sys.getfilesystemencoding())
# print(decodePath(DIRN))

def main():
    try:
        f = ftplib.FTP(HOST)
        f.encoding = 'utf-8'
        f.sendcmd("OPTS UTF8 ON")

        # f.__class__.encoding = 'cp1251' # sys.getfilesystemencoding()
        f.__class__.encoding = 'utf-8'
    except (socket.error, socket.gaierror) as e:
        print('ERROR: невозможно подключиться к "%s"' % HOST )
        return
    print('*** Подклчены к хосту "%s"' % HOST)

    try:
        f.login(user=user, passwd=passwd)
    except ftplib.error_perm:
        print('ERROR: невозможно подключиться под "%s"' % user)
        return
    print('*** Подклчены к хосту "%s" под "%s"' % (HOST, user))

    try:
        f.login(user=user, passwd=passwd)
    except ftplib.error_perm:
        print('ERROR: невозможно подключиться под "%s"' % user)
        return
    print('*** Подклчены к хосту "%s" под "%s"' % (HOST, user))
    # print(path = DIRN.encode('cp1251').decode()('cp1251'))
    print(f.encoding)
    # print(locale.getpreferredencoding(False))
    # for i in f.mlsd():
    # f.retrlines('LIST')
    print(f.encoding)
    print()

    try:
        f.cwd(DIR_analiz_reag)
        for i in f.mlsd(DIR_analiz_reag):
            print(i[0])
    except ftplib.error_perm:
        print('ERROR: невозможно открыть каталог "%s"' % DIR_analiz_reag)
        f.quit()
        return
    print('*** Перемещены в каталог "%s"' % DIR_analiz_reag)
    # for i in f.mlsd(DIR_analiz_reag):
    #     print(i[0])

    if 'Московская область' in [i[0] for i in f.mlsd(DIR_analiz_reag)]:
        f.cwd(DIR_mos_obl)
        files_list = f.nlst()
        print(files_list)
        for file_name in files_list:
            if 'порубочн'in file_name:
                print(file_name)
                try:
                    file_path = os.path.join(dir_local_y_m_d, file_name)
                    f.retrbinary('RETR %s' % file_name, open(file_path, 'wb').write)
                except ftplib.error_perm:
                    print('нет доступа к файлу "%s"' % file_name)
                    if os.path.exists(file_name):
                        os.unlink(file_name)
                else:
                    print('*** Скачан "%s" to CWD' % file_name)

                break
                # pass
        print(file_name)
    else:
        print('Папка "Московская область" еще не создана на FTP-сервере')
    f.quit()


if __name__ == '__main__':
    main()