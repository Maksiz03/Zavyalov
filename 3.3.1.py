import pandas as pd
import datetime


from dateutil.relativedelta import relativedelta


currensy = {'nan': 1928667, 'USD': 167994, 'RUR': 1830967, 'EUR': 10641, 'KZT': 65291, 'UAH': 25969, 'BYR': 41178,
            'AZN': 607, 'UZS': 2966, 'KGS': 645, 'GEL': 36}
list2 = ['USD', 'RUR', 'EUR', 'KZT', 'UAH', 'BYR']
rows_list = []


def getapi(date):
    date = str(date).split('-')
    url = 'http://www.cbr.ru/scripts/XML_daily.asp?date_req={0}/{1}/{2}'.format(date[2], date[1], date[0])
    tempData = (pd.read_xml(url, encoding='cp1251'))
    dict1 = {}
    dict1['date'] = str(f'{date[0]}-{date[1]}')
    dict1['USD'] = float(
        (str(tempData['Value'].loc[(tempData.index[tempData[tempData['CharCode'] == 'USD'].index[0]])])).replace(',',
                                                                                                                 '.')) / int(
        (str(tempData['Nominal'].loc[(tempData.index[tempData[tempData['CharCode'] == 'USD'].index[0]])])))
    dict1['EUR'] = float(
        (str(tempData['Value'].loc[(tempData.index[tempData[tempData['CharCode'] == 'EUR'].index[0]])])).replace(',',
                                                                                                                 '.')) / int(
        (str(tempData['Nominal'].loc[(tempData.index[tempData[tempData['CharCode'] == 'EUR'].index[0]])])))
    try:
        dict1['KZT'] = float(
            (str(tempData['Value'].loc[(tempData.index[tempData[tempData['CharCode'] == 'KZT'].index[0]])])).replace(
                ',',
                '.')) / int(
            (str(tempData['Nominal'].loc[(tempData.index[tempData[tempData['CharCode'] == 'KZT'].index[0]])])))
    except IndexError:
        dict1['KZT'] =''
    try:
        dict1['UAH'] = float(
            (str(tempData['Value'].loc[(tempData.index[tempData[tempData['CharCode'] == 'UAH'].index[0]])])).replace(
                ',',
                '.')) / int(
            (str(tempData['Nominal'].loc[(tempData.index[tempData[tempData['CharCode'] == 'UAH'].index[0]])])))
    except IndexError:
        dict1['UAH'] =''
    try:
        dict1['BYR'] = float(
            (str(tempData['Value'].loc[(tempData.index[tempData[tempData['CharCode'] == 'BYR'].index[0]])])).replace(
                ',',
                '.')) / int(
            (str(tempData['Nominal'].loc[(tempData.index[tempData[tempData['CharCode'] == 'BYR'].index[0]])])))
    except IndexError:
        dict1['BYR'] =''
    print(dict1)
    rows_list.append(dict1)


dataframe_dev = pd.read_csv("vacancies_dif_currencies.csv")
dataframe_dev = dataframe_dev[dataframe_dev.salary_currency.isin(list2) == True]
dataframe_dev['published_at'] = dataframe_dev['published_at'].apply(
    lambda v: datetime.datetime.strptime(v[:10], '%Y-%m-%d'))
startdate = str(dataframe_dev['published_at'].min())[:10].split('-')
endDate = str(dataframe_dev['published_at'].max())[:10].split('-')
startdate = datetime.date(int(startdate[0]), int(startdate[1]), int(startdate[2]))
endDate = datetime.date(int(endDate[0]), int(endDate[1]), int(endDate[2]))
delta = datetime.timedelta(days=30)
date_after_month = relativedelta(months=1)
while startdate <= endDate:
    getapi(startdate)
    startdate += date_after_month
df = pd.DataFrame(rows_list)
print(df)
df.to_csv('my_data.csv', index=False)
