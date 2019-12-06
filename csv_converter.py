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
