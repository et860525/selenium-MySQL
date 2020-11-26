from datetime import datetime
import matplotlib
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd

import read_db

date = []
close = []

#df = pd.DataFrame(data=data, columns=['date','open','high','low','close','adj_close','volume'])

def data_from_csv(filename):
    data = pd.read_csv('AAPL.csv') # filename
    try:
        for row in data['Date']:
            # matplotlib.dates.date2num(): Convert datetime objects to Matplotlib dates.
            # datetime.strptime(row[0], "%Y-%m-%d"): Translate string to datetime object.
            date.append(matplotlib.dates.date2num(datetime.strptime(row, "%Y-%m-%d")))
        
        for row in data['Close']:
            close.append(row)

        ax = plt.gca() # Get axes and draw (獲得軸線可進行繪畫)

        ax.xaxis.set_major_locator(matplotlib.dates.MonthLocator()) # Find Month set main xaxis
        ax.xaxis.set_major_formatter(matplotlib.dates.DateFormatter('%m')) # Set fomat for xaxis

        plt.plot(date, close, linewidth=1)
        plt.show()   
    except:
        pass


def data_from_db(stock_name):
    from connection import db_config
    import pymysql

    # Declear data first ?

    try:
        params = db_config.config()
        conn = pymysql.connect(**params)
        cursor = conn.cursor()

        cursor.execute(f"SELECT date, close FROM {stock_name}")

        data = cursor.fetchall()

    except pymysql.DatabaseError as err:
        print("Something went wrong: {}".format(err))
    finally:
        conn.close()

    try:
        for row in data:
            # matplotlib.dates.date2num(): Convert datetime objects to Matplotlib dates.
            # datetime.strptime(row[0], "%Y-%m-%d"): Translate string to datetime object.
            date.append(matplotlib.dates.date2num(datetime.strptime(row[0], "%Y-%m-%d")))
            close.append(row[1])

        ax = plt.gca() # Get axes and draw (獲得軸線可進行繪畫)
        
        # Test 軸線繪畫，將上面的line與右邊的line，設為隱藏
        #ax.spines['right'].set_color('none')
        #ax.spines['top'].set_color('none')
    
        ax.xaxis.set_major_locator(matplotlib.dates.MonthLocator()) # Find Month set main xaxis
        ax.xaxis.set_major_formatter(matplotlib.dates.DateFormatter('%m')) # Set fomat for xaxis

        plt.plot(date, close, linewidth=1)
        plt.show()   
    except:
        pass
