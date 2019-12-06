import sqlite3
import pandas as pd
from sqlalchemy import create_engine

'''This script will used to insert all sql data into database
   Doing Operations on database is faster than using raw excel/csv file
   If you have more RAM in your machine then you can use this script to load your database into RAM
'''

engine = create_engine('sqlite:///new_data.db') #Create New Database File
#We can use 'sqlite://' to use database inside your RAM so large data will parse easily
df = pd.read_csv('bitcoin_data.csv')
df.to_sql('bitcoin_data', engine, if_exists='replace', index=False) #Create Table with name=bitcoin_data

results = engine.execute('SELECT * FROM bitcoin_data ORDER BY High DESC LIMIT 1;')
MAX_result = pd.DataFrame(results, columns=df.columns)
print('MAX_HIGH \n',MAX_result)

results = engine.execute('SELECT * FROM bitcoin_data ORDER BY High ASC LIMIT 1;')
MIN_result = pd.DataFrame(results, columns=df.columns)
print('MIN_HIGH: \n',MAX_result)

results = engine.execute('SELECT SUM(Volume) FROM bitcoin_data;')
total_volume = pd.DataFrame(results)
print('TOTAL VOLUME TRADED:',total_volume)
