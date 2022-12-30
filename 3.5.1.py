
import csv, sqlite3
import pandas as pd


df = pd.read_csv('my_data.csv')

df.columns = df.columns.str.strip()

connection = sqlite3.connect('demo.db')

df.to_sql('housing_development',connection, if_exists='replace')