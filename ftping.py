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
# delta = timedelta(days=1)
# dt_now = dt_now - delta

# print(dt_now.strftime('%B'))
# print(dt_now.strftime('%Y'))

r_dir_analiz_reag = '/Электронный архив/6.ЦФО/#Материалы_для_ежедневного_селекторного_совещания/' + dt_now.strftime('%Y') \
       + '/' + dt_now.strftime('%m') + '. ' + dt_now.strftime('%B') + ' ' + dt_now.strftime('%Y') + '/' + \
       dt_now.strftime('%d.%m.%Y') + '/Анализ реагирования'

r_dir_mos_obl = r_dir_analiz_reag + '/Московская область'

l_dir = '\\\\'+LOCALHOST+'\\shara\\Оперативный дежурный\\!_левая машина\\1_ОПЕРАТИВНЫЙ ДЕЖУРНЫЙ\\Планируемые сжигания порубочных остатков от МО'




def check_l_dirs_exist(l_dir):
    l_dir_y = os.path.join(l_dir, dt_now.strftime('%Y'))
    if os.path.exists(l_dir_y):
        print('локальная %s папка существует ' % dt_now.strftime('%Y'))
    else:
        os.mkdir(l_dir_y)
        print('создана папка %s' % dt_now.strftime('%Y'))

    l_dir_y_m = os.path.join(l_dir_y, dt_now.strftime('%B'))
    if os.path.exists(l_dir_y_m):
        print('локальная %s папка существует ' % dt_now.strftime('%B'))
    else:
        os.mkdir(l_dir_y_m)
        print('создана папка %s' % dt_now.strftime('%B'))

    l_dir_y_m_d = os.path.join(l_dir_y_m, dt_now.strftime('%d.%m.%Y'))
    if os.path.exists(l_dir_y_m_d):
        print('локальная %s папка существует ' % dt_now.strftime('%d.%m.%Y'))

    else:
        os.mkdir(l_dir_y_m_d)
        print('создана папка %s' % dt_now.strftime('%d.%m.%Y'))

    return l_dir_y_m_d
# print(sys.getdefaultencoding())
# print(sys.getfilesystemencoding())

def check_ftp_connect(HOST, user, passwd):
    try:
        f = ftplib.FTP(HOST)
        f.encoding = 'utf-8'
        f.sendcmd("OPTS UTF8 ON")
        # f.__class__.encoding = 'cp1251' # sys.getfilesystemencoding()
        f.__class__.encoding = 'utf-8'
    except (socket.error, socket.gaierror) as e:
        print('ERROR: невозможно подключиться к "%s"' % HOST )
        return None
    print('*** Подклчены к хосту "%s"' % HOST)

    try:
        f.login(user=user, passwd=passwd)
    except ftplib.error_perm:
        print('ERROR: невозможно подключиться под "%s"' % user)
        return None
    print('*** Подклчены к хосту "%s" под "%s"' % (HOST, user))

    try:
        f.cwd(r_dir_analiz_reag)
        # for i in f.mlsd(r_dir_analiz_reag):
        #     # print(i[0])
        if 'Московская область' in [i[0] for i in f.mlsd(r_dir_analiz_reag)]:
            return f
        else:
            print('Папка "Московская область" еще не создана на FTP-сервере')
        f.quit()
    except ftplib.error_perm:
        print('ERROR: невозможно открыть каталог "%s"' % r_dir_analiz_reag)
        f.quit()
        return None
    # print('*** Перемещены в каталог "%s"' % r_dir_analiz_reag)

# print(f.__class__.encoding = sys.getfilesystemencoding())
# print(decodePath(DIRN))


def copy_felling_residues_file(f, l_dir_y_m_d):
    f.cwd(r_dir_mos_obl)
    files_list = f.nlst()
    print(files_list)
    for file_name in files_list:
        if 'порубочн' in file_name or 'жиган' in file_name or 'ПО' in file_name:
            print(file_name)
            file_path = os.path.join(l_dir_y_m_d, file_name)
            copy_file(f, file_path, file_name)
            break
            # pass               # print(file_name)

def copy_file(f, file_path, file_name):
    try:
        f.retrbinary('RETR %s' % file_name, open(file_path, 'wb').write)
    except ftplib.error_perm:
        print('нет доступа к файлу "%s"' % file_name)
        if os.path.exists(file_name):
            os.unlink(file_name)
    else:
        print('*** Скачан "%s" to CWD' % file_name)

def main():
    l_dir_y_m_d = check_l_dirs_exist(l_dir)
    if not os.listdir(l_dir_y_m_d):
        f = check_ftp_connect(HOST, user, passwd)
        copy_felling_residues_file(f, l_dir_y_m_d) if f else print('На удаленном сервере нет требуемых файлов')
    else:
        print('папке %s уже не пустая' % l_dir_y_m_d)

    # f = check_ftp_connect(HOST, user, passwd)
    # copy_felling_residues_file(f, l_dir_y_m_d) if f else print('На удаленном сервере нет требуемых файлов')




if __name__ == '__main__':
    main()