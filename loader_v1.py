
from threading import Thread
import threading

import numpy as np
import time
import csv
import pandas as pd
import matplotlib.pyplot as plt

path = "/home/pi/Documents/PYPM2022/testdata/"
file = "test.csv"

frame = pd.read_csv(path+file)
f = frame.set_index('0')

for index, row in f.iterrows():
    plt.plot(row, label=index)

    
    
    
plt.show()