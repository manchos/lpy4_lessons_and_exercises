import requests

def get_weather(url):
    result = requests.get(url)
    if result.status_code == 200:
        return result.json()
    else:
        print("Что то пошло не так")


if __name__ == '__main__':
    data = get_weather('http://api.openweathermap.org/data/2.5/weather?id=524901&units=metric&APPID=9c34053cfb0f9d9c9e6c797581ab0f09')
    print(data)