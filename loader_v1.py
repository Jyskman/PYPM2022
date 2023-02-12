
from threading import Thread
import threading

import numpy as np
import time
import csv
import pandas as pd
import matplotlib.pyplot as plt

path = "/media/pi/GAME DEV/Data/"
file = "Start_2023_02_11_17_10_22.csv"

frame = pd.read_csv(path+file)
f = frame.set_index('0')

# for index, row in f.iterrows():
#     plt.plot(row, label=index)
# 
#     
    
    
plt.show()

# sista 4
# f.iloc[:,-4:]