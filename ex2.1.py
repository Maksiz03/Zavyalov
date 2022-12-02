import csv
import math
import re




dict = {}
cities = {}
# file = input()
with open("vacancies.csv", encoding='utf_8') as file:
    count = 0
    maxSalary = 0
    lowSalary = 9999999
    countCities = 0
    readerFile = csv.reader(file)
    title = next(readerFile)
    vacancyData = []
    title[0] = 'name'
    for vacancy in readerFile:
        if len(vacancy) < len(title):
            continue
        is_correct_string = True
        for check_line in vacancy:
            if len(check_line) == 0:
                is_correct_string = False
                break
        if is_correct_string:
            vacancyData.append(vacancy)
            for keys, val in enumerate(vacancy):
                temp = re.sub(re.compile(r'<[^>]+>'), '', val)
                temp = temp.replace('\n', ', ')
                temp = temp.replace('\r\n', ', ')
                temp = ' '.join(temp.split())
                dict[title[keys]] = temp
            if dict['salary_currency'] == 'RUR':
                if cities.keys().__contains__(dict['area_name']):
                    cities[dict['area_name']] += 1
                else:
                    cities[dict['area_name']] = 1
                    countCities += 1
                if math.floor(cities[dict['area_name']]/35) >= 0.01:
                    if int(dict['salary_to']) > maxSalary:
                        maxSalary = int(dict['salary_to'])
                    if int(dict['salary_from']) < lowSalary:
                        lowSalary = int(dict['salary_from'])

    print(f'{maxSalary}')
