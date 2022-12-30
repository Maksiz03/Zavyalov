import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import report as report
from matplotlib.backends.backend_pdf import PdfPages
import pdfkit

file = input('Введите название файла: ')
profession = input('Введите название профессии: ')

vacancy = pd.read_csv('vacancies_dif_currencies.csv')
course = pd.read_csv('my_data.csv')

isSalaryFrom = pd.isnull(vacancy["salary_from"])
isSalaryTo = pd.isnull(vacancy["salary_to"])
isCyrr = pd.isnull(vacancy["salary_currency"])
vacancy['salary'] = ''

for i in range(vacancy.shape[0]):
    publiched = vacancy['published_at'].loc[vacancy.index[i]][:7]
    if (vacancy.loc[i, 'salary_from'] > 1) == True and (vacancy.loc[i, 'salary_to'] > 1) == True:
        try:
            if vacancy['salary_currency'].loc[vacancy.index[i]] != 'RUR':
                vacancy['salary'].loc[vacancy.index[i]] = ((vacancy["salary_from"].loc[vacancy.index[i]] + (
                    vacancy["salary_to"].loc[vacancy.index[i]])) / 2) * course.loc[course['date'] == publiched][
                                                              vacancy['salary_currency'].loc[vacancy.index[i]]]
            else:
                vacancy['salary'].loc[vacancy.index[i]] = ((vacancy["salary_from"].loc[vacancy.index[i]] + (
                    vacancy["salary_to"].loc[vacancy.index[i]])) / 2)
        except:
            vacancy['salary'].loc[vacancy.index[i]] = ' '
    elif (vacancy.loc[i, 'salary_from'] > 1) == True and (vacancy.loc[i, 'salary_to'] < 1) == False:
        try:
            if vacancy['salary_currency'].loc[vacancy.index[i]] != 'RUR':
                vacancy['salary'].loc[vacancy.index[i]] = (vacancy["salary_from"].loc[vacancy.index[i]]) * \
                                                          course.loc[course['date'] == publiched][
                                                              vacancy['salary_currency'].loc[
                                                                  vacancy.index[i]]]  # вот так надо
            else:
                vacancy['salary'].loc[vacancy.index[i]] = (vacancy["salary_from"].loc[vacancy.index[i]])
        except:
            vacancy['salary'].loc[vacancy.index[i]] = ' '
    elif (vacancy.loc[i, 'salary_from'] < 1) == False and (vacancy.loc[i, 'salary_to'] > 1) == True:
        try:
            if vacancy['salary_currency'].loc[vacancy.index[i]] != 'RUR':
                vacancy['salary'].loc[vacancy.index[i]] = (vacancy["salary_to"].loc[vacancy.index[i]]) * \
                                                          course.loc[course['date'] == publiched][
                                                              vacancy['salary_currency'].loc[vacancy.index[i]]]
            else:
                vacancy['salary'].loc[vacancy.index[i]] = (vacancy["salary_to"].loc[vacancy.index[i]])
        except:
            vacancy['salary'].loc[vacancy.index[i]] = ' '
    else:
        vacancy['salary'].loc[vacancy.index[i]] = ' '
    print(i)
vacancy = vacancy[vacancy.salary != ' ']
vacancy.pop('salary_to')
vacancy.pop('salary_from')
vacancy.pop('salary_currency')
new_vacancy = vacancy[['name', 'salary', 'area_name', 'published_at']]
new_vacancy['published_at'] = new_vacancy['published_at'].str.split('-').str.get(0)
SalaryForYear1 = new_vacancy.groupby('published_at').agg({'salary': 'mean'})
CountForYear1 = new_vacancy.groupby('published_at').size()
filterProfDf = new_vacancy[new_vacancy['name'].str.contains('аналитик', case=False)]
SalaryForYear2 = filterProfDf.groupby('published_at').agg({'salary': 'mean'})
CountForYear2 = filterProfDf.groupby('published_at').size()
result = pd.concat([SalaryForYear1, CountForYear1, SalaryForYear2, CountForYear2], axis='columns')
result.columns = ['salaryAll', 'countAll', 'salaryProf', 'countProf']
result.to_csv('stat.csv')

fig, ax = plt.subplots(figsize=(12, 4))
ax.axis('tight')
ax.axis('off')
the_table = ax.table(cellText=result.values, colLabels=result.columns, loc='center')

# https://stackoverflow.com/questions/4042192/reduce-left-and-right-margins-in-matplotlib-plot
pp = PdfPages("foo.pdf")
pp.savefig(fig, bbox_inches='tight')
pp.close()

