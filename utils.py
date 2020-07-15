import json


def city():
    f = open('Data/city.json')
    data = json.load(f)
    li = []
    for i in data:
        if i['country'] == 'IN':
            li.append([i['id'], i['name']])
    return li


def clean(data):
    result = []
    humidity = data['main']['humidity']
    w = data['weather'][0]['main']
    K = data['main']['temp']
    c = round(K - 273.15, 2)
    f = round((c*(9/5))+32, 2)
    result.append(data['name'])
    result.append([c, f])
    result.append(w)
    result.append(humidity)
    return result
