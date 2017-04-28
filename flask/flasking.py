from flask import Flask, request, render_template
import requests
from weather import get_weather
from datetime import datetime
import sys
import locale
import re
from news_list import all_news

city_id = 524901
apikey = '9c34053cfb0f9d9c9e6c797581ab0f09'
dt_now = datetime.now()

if sys.platform == 'win32':
    locale.setlocale(locale.LC_ALL, 'rus_rus')
else:
    locale.setlocale(locale.LC_ALL, 'ru_RU.UTF-8')

app = Flask(__name__)



@app.route('/weather/')
def weather():
    url = "http://api.openweathermap.org/data/2.5/weather?id=%s&units=metric&APPID=%s" % (city_id, apikey)
    weather = get_weather(url)
    result = '<p>Температура: %s</p>' % weather['main']['temp']
    result += "<p>Город: %s</p>" % weather['name']
    result += "<p>Дата: %s</p>" % dt_now.strftime('%d.%m.%Y')
    return result

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/news/limit')
def news_limit():
    colors = ['blue', 'yellow', 'red', 'green', 'magenta']
    # for item in request.args:
    #     print(item)
    #     print(request.args.get(item))
    try:
        limit = int(request.args.get('limit'))
    except:
        limit = 10
    color = request.args.get('color', 'black') if request.args.get('color') in colors else 'black'
    return '<h1 style="color: %s">News: <small>%s</small></h1>' % (color, limit)

@app.route('/login/', methods=['POST'])
def login():
    return render_template('login.html', email=request.form.get('email'), password=request.form.get('passwd'))


@app.route('/news/all')
def all_the_news():
    colors = ['blue', 'yellow', 'red', 'green', 'magenta']
    # for item in request.args:
    #     print(item)
    #     print(request.args.get(item))
    try:
        limit = int(request.args.get('limit'))
    except:
        limit = 10
    color = request.args.get('color', 'black') if request.args.get('color') in colors else 'black'
    return render_template('all_the_news.html')


@app.route('/news/<int:news_id>')
def news_by_id(news_id):
    news_to_show = [news for news in all_news if news['id'] == news_id]
    if len(news_to_show) == 1:
        date_show = (datetime.strptime(news_to_show[0]['date'], '%Y-%m-%d')).strftime('%d.%m.%Y')
        result = "<h1>%s</h1><p><i>%s</i></p><p><i>%s</i></p>"
        result = result % (news_to_show[0]['title'], date_show, news_to_show[0]['text'])
            # 'Новость: %s' % news_id
        return result
    else:
        abort(404)

@app.route('/names/')
def newborn_names_info():
    year = 0
    try:
        year = request.args.get('year')
        val_year = re.search(r'201\d+', year)
        year = val_year.group(0)
    except:
        year = 0
    names_request = requests.get('https://apidata.mos.ru/v1/datasets/2009/rows')
    if names_request.status_code == 200:
        newborn_names_list = names_request.json()
    if year:
        return render_template('names.html', newborn_names_list=
        [newborn_name['Cells'] for newborn_name in newborn_names_list if newborn_name['Cells']['Year'] == int(year)])
    else:
        return render_template('names.html', newborn_names_list=
        [newborn_name['Cells'] for newborn_name in newborn_names_list])

if __name__ == '__main__':
    app.run()
