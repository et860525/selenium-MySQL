from datetime import datetime
import matplotlib
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd

import read_db

date = []
close = []

data = read_db.get_data()
try:
    #df = pd.DataFrame(data=data, columns=['date','open','high','low','close','adj_close','volume'])

    for row in data:
        date.append(matplotlib.dates.date2num(datetime.strptime(row[0], "%Y-%m-%d")))
        close.append(row[4])
    ax = plt.gca()
    ax.xaxis.set_major_locator(matplotlib.dates.MonthLocator())
    ax.xaxis.set_major_formatter(matplotlib.dates.DateFormatter('%m'))
    #ax.tick_params(pad=20)

    plt.plot(date, close, linewidth=0.5)
    plt.show()   


except:
    pass