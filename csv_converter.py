import sqlite3
import pandas as pd
from sqlalchemy import create_engine

engine = create_engine('sqlite:///new_data.db')
df = pd.read_csv('bitcoin_data.csv')
df.to_sql('bitcoin_data', engine, if_exists='replace', index=False)
