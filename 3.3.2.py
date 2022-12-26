import pandas as pd


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
                vacancy["salary_to"].loc[vacancy.index[i]])) / 2) * course.loc[course['date'] == publiched][ vacancy['salary_currency'].loc[vacancy.index[i]]]
            else:
                vacancy['salary'].loc[vacancy.index[i]] = ((vacancy["salary_from"].loc[vacancy.index[i]] + (
                    vacancy["salary_to"].loc[vacancy.index[i]])) / 2)
        except:
            vacancy['salary'].loc[vacancy.index[i]] = ' '
    elif (vacancy.loc[i, 'salary_from'] > 1) == True and (vacancy.loc[i, 'salary_to'] < 1) == False:
        try:
            if vacancy['salary_currency'].loc[vacancy.index[i]] != 'RUR':
                vacancy['salary'].loc[vacancy.index[i]] = (vacancy["salary_from"].loc[vacancy.index[i]])*course.loc[course['date'] == publiched][ vacancy['salary_currency'].loc[vacancy.index[i]]]  # вот так надо
            else:
                vacancy['salary'].loc[vacancy.index[i]] = (vacancy["salary_from"].loc[vacancy.index[i]])
        except:
            vacancy['salary'].loc[vacancy.index[i]] = ' '
    elif (vacancy.loc[i, 'salary_from'] < 1) == False and (vacancy.loc[i, 'salary_to'] > 1) == True:
        try:
            if vacancy['salary_currency'].loc[vacancy.index[i]] != 'RUR':
                vacancy['salary'].loc[vacancy.index[i]] = (vacancy["salary_to"].loc[vacancy.index[i]])*course.loc[course['date'] == publiched][ vacancy['salary_currency'].loc[vacancy.index[i]]]
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
new_vacancy = vacancy[['name','salary','area_name','published_at']]
new_vacancy.to_csv('salary.csv', index=False)
