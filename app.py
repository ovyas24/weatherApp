import requests
from flask import Flask, render_template
from flask import request, redirect
from utils import *


app = Flask(__name__)


def weather(text):
    wdata = []
    cities = text.lower().replace(',', ' ').split()
    for city in cities:
        response = requests.get(
            f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=f3232d76c8092c56b0f75fb1dbe9ffa9')
        data = response.json()
        try:
            wdata.append(clean(data))
        except:
            pass
    return wdata


@app.route('/')
def index():
    return render_template('index.html', hidden=True)


@app.route('/', methods=['POST'])
def weather_search():
    text = request.form['text']
    data = weather(text)
    return render_template('index.html', weather=data, hidden=False)


@app.route('/citydata')
def cities():
    li = city()
    return render_template('city.html', city=li)


if __name__ == '__main__':
    app.run(debug=True)
