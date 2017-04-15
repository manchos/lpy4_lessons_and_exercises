import csv
import collections
import requests

"""
Остановки
Считать из csv-файла (с http://data.mos.ru/datasets/752) количество остановок,
вывести улицу, на которой больше всего остановок.
"""
# with open('files/moscow_trans_stops.csv', 'r', encoding='utf-8') as f:
#     for line in f:
#         fields = line.split(";"))
#         break
count = collections.Counter()

with open('files/moscow_trans_stops.csv', 'r', encoding='utf-8') as f:
    for line in f:
        fields = line.split(";")
        break
    reader = csv.DictReader(f, fields, delimiter=';')
    trans_stops_count = 0
    for x in [x['Street'] for x in reader]:
        trans_stops_count += 1
        count[x] += 1
    print("Количество остановок: %s" % trans_stops_count)
    print(count)
    print("Улица, на которой больше всего остановок: %s" % count.most_common(1)[0][0])


#============================================================================================
    names_request = requests.get('https://apidata.mos.ru/v1/datasets/2009/rows')
    if names_request.status_code == 200:
        newborn_names_list = names_request.json()
        print(newborn_names_list)

