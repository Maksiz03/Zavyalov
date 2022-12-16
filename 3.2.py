import pandas as pd
import datetime
from datetime import datetime



pd.set_option("expand_frame_repr", False)


file="vacancies_by_year.csv"
df = pd.read_csv(file)


df['years'] = df['published_at'].apply(lambda x: datetime.strptime(x,"%Y-%m-%dT%H:%M:%S%z").year)
print (df.head(10))
years = df['years'].unique()
for year in years:
    data = df[df["years"]==year]
    data[['name','salary_from','salary_to','salary_currency','area_name','published_at']].to_csv(rf"csv_files\part_{year}.csv", index=False)