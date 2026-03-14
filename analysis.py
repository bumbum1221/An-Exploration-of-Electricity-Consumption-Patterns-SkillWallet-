import pandas as pd

import sqlite3

df = pd.read_csv("Consumption.csv")

print(df.head())

df['Dates'] = pd.to_datetime(df['Dates'], dayfirst=True)
df = df.dropna()
df = df.sort_values('Dates')


import sqlite3

conn = sqlite3.connect("electricity.db")

df.to_sql("consumption", conn, if_exists="replace", index=False)

conn.close()

print("Database created!")