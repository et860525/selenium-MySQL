import sys
from pathlib import Path
p = Path.cwd().parent
sys.path.append(str(p))

import pymysql
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from connection.db_config import config

data = None
def get_data():
    try:
        params = config()
        conn = pymysql.connect(**params)

        cursor = conn.cursor()
        cursor.execute('SELECT date,open,high,low,close,adj_close,volume FROM aapl')

        data = cursor.fetchall()
        
        conn.close()

        return data
    except:
        print('Error')