import sys
from pathlib import Path

import pymysql
import pandas as pd

p = Path.cwd().parent
sys.path.append(str(p))

from connection import db_config

data = pd.read_csv('AAPL.csv')
df = pd.DataFrame(data)

def insert_aapl():
    try:
        params = db_config.config()

        conn = pymysql.connect(**params)
        cursor = conn.cursor()
        for row in df.itertuples(index=False):
            cursor.execute('''INSERT INTO aapl(date, open, high, low, close, adj_close, volume) 
                VALUES('{}',{},{},{},{},{},{})'''.format(row[0],row[1],row[2],row[3],row[4],row[5],row[6]))

        conn.commit()
        print('Success')

        conn.close()
    except:
        pass    