from flask import Flask
from weather import get_weather
from datetime import datetime
import sys
import locale
from news_list import all_news

city_id = 524901
apikey = '9c34053cfb0f9d9c9e6c797581ab0f09'
dt_now = datetime.now()

if sys.platform == 'win32':
    locale.setlocale(locale.LC_ALL, 'rus_rus')
else:
    locale.setlocale(locale.LC_ALL, 'ru_RU.UTF-8')

app = Flask(__name__)



@app.route('/')
def index():
    url = "http://api.openweathermap.org/data/2.5/weather?id=%s&units=metric&APPID=%s" % (city_id, apikey)
    weather = get_weather(url)
    result = '<p>Температура: %s</p>' % weather['main']['temp']
    result += "<p>Город: %s</p>" % weather['name']
    result += "<p>Дата: %s</p>" % dt_now.strftime('%d.%m.%Y')
    return result

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

if __name__ == '__main__':
    app.run()
