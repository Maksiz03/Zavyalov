
import matplotlib.pyplot as plt
import numpy as np

DobacilNum=1
width =0.35
dictSalaryForYear = {2007: 38916, 2008: 43646, 2009: 42492, 2010: 43846, 2011: 47451, 2012: 48243, 2013: 51510, 2014: 50658}
dictSalaryForYearForProf = {2007: 43770, 2008: 50412, 2009: 46699, 2010: 50570, 2011: 55770, 2012: 57960, 2013: 58804, 2014: 62384}
dictCountVacansy= {2007: 2196, 2008: 17549, 2009: 17709, 2010: 29093, 2011: 36700, 2012: 44153, 2013: 59954, 2014: 66837}
dictCountVacansyForProf ={2007: 317, 2008: 2460, 2009: 2066, 2010: 3614, 2011: 4422, 2012: 4966, 2013: 5990, 2014: 5492}
dictLevelSalaryForYearForCity = {"Москва": 57354, "Санкт-\nПетербург": 46291, "Новосибирск": 41580, "Екатеринбург": 41091, "Казань": 37587, "Самара": 34091, "Нижний\nНовгород": 33637, "Ярославль": 32744, "Краснодар": 32542, "Воронеж": 29725}
dictPercentVacancyForcity = {"Другие": 0.2755, "Москва": 0.4581,"Санкт-Петербург": 0.1415, "Нижний Новгород": 0.0269, "Казань": 0.0266, "Ростов-на-Дону": 0.0234, "Новосибирск": 0.0202, "Екатеринбург": 0.0143, "Воронеж": 0.014, "Самара": 0.0133, "Краснодар": 0.0131 }

labels = dictSalaryForYear.keys()
x = np.arange(len(dictSalaryForYear.keys()))




fig, ax = plt.subplots(2,2)
rect1 = ax[0,0].bar(x - width/2, dictSalaryForYear.values(),width, label='средняя з/п')
rect2 = ax[0,0].bar(x + width/2, dictSalaryForYearForProf.values(),width, label='з/п программиста')
rect3 = ax[0,1].bar(x - width/2, dictCountVacansy.values(),width, label='Количество вакансий')
rect4 = ax[0,1].bar(x + width/2, dictCountVacansyForProf.values(),width, label='Количество вакансий программист')


y_pos = np.arange(len(dictLevelSalaryForYearForCity.keys()))
performance = dictLevelSalaryForYearForCity.values()
ax[1,0].barh(y_pos, performance, align='center')
ax[1,0].set_yticks(y_pos, labels=dictLevelSalaryForYearForCity.keys(),size =6)
ax[1,0].invert_yaxis()
ax[1,0].set_title('Уровень зарплат по городам')


ax[1,1].pie(dictPercentVacancyForcity.values(), labels=dictPercentVacancyForcity.keys(),textprops={'fontsize': 6})
ax[1,1].set_title('Доля вакансий по городам')

ax[0,0].set_title('Уровень зарплат по годам')
ax[0,0].set_xticks(x)
ax[0,0].set_xticklabels(labels)
ax[0,0].legend()
ax[0,1].set_title('Количество вакансий по годам')
ax[0,1].set_xticks(x)
ax[0,1].set_xticklabels(labels)
ax[0,1].legend()

fig.tight_layout()
ax[0,0].grid(axis = 'y')
ax[1,0].grid(axis = 'x')

ax[0,0].tick_params(axis='x', labelrotation=90)

ax[0,1].grid(axis = 'y')

ax[0,1].tick_params(axis='x', labelrotation=90)
plt.savefig('figure.png')

plt.show()