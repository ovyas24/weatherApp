import requests
import json
from flask import Flask,render_template

app = Flask(__name__)

def city():
    f = open('Data/city.json')
    data = json.load(f)
    li = []
    for i in data:
        if i['country'] == 'IN':
            li.append([i['id'],i['name']])
    return li

def clean(data):
    result = []
    humidity = data['main']['humidity']
    K = data['main']['temp']
    c = round(K - 273.15,2)
    f = round((c*(9/5))+32,2)
    result.append(data['name'])
    result.append([c,f])
    result.append(humidity)
    return result

def weather():
    wdata = []
    cities = ['faridabad','delhi','kochi','mumbai','patna']
    for city in cities:
        response = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=f3232d76c8092c56b0f75fb1dbe9ffa9')
        data = response.json()
        wdata.append(clean(data))
    print('Data recived')
    return wdata

@app.route('/')
def index():
    data = weather()
    return render_template('index.html',weather=data)


@app.route('/citydata')
def cities():
    li = city()
    return render_template('city.html',city = li)


if __name__ == '__main__':
    app.run(debug=True)