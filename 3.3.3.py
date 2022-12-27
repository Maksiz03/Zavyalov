import json
import requests
import time
import pandas as pd


def getPage(page=0):
    """
    Создаем метод для получения страницы со списком вакансий.
    Аргументы:
        page - Индекс страницы, начинается с 0. Значение по умолчанию 0, т.е. первая страница
    """

    params = {
        'specialization': 1,
        'date_from': '2022-12-10',
        'date_to': '2022-12-10',
        'page': page,
        'per_page': 100
    }

    req = requests.get('https://api.hh.ru/vacancies', params)
    data = req.content.decode()
    req.close()
    return data


for page in range(0, 30):

    jsObj = json.loads(getPage(page))
    nextFileName = 'search.json'

    f = open(nextFileName, mode='w', encoding='utf8')
    f.write(json.dumps(jsObj, ensure_ascii=False))
    f.close()

    if (jsObj['pages'] - page) <= 1:
        break

    time.sleep(0.25)
    print(1)
print('Старницы поиска собраны')
dt = []
df2 = pd.read_json('search.json')
for js in df2['items']:
    if js['salary'] != None:
        salary_from = js['salary']['from']
        salaty_to = js['salary']['to']
        salary_currency = js['salary']['currency']
    else:
        salary_from = None
        salaty_to = None
        salary_currency = None
    dt.append([
        js['name'],
        salary_from,
        salaty_to,
        salary_currency,
        js['published_at'],
        ])

df = pd.DataFrame(dt, columns=['name', 'salary_from', 'salary_to','salary_currency','published_at'])
df.to_csv('searchHH.csv', index=False)

