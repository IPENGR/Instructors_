#Histogram
#A histogram needs only one column.
#A histogram shows us the frequency of each interval
#Three lines to make our compiler able to draw:
import sys
import matplotlib
matplotlib.use('Agg')

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data2.csv')

df["Duration"].plot(kind = 'hist')

plt.show()

#Two lines to make our compiler able to draw:
plt.savefig(sys.stdout.buffer)
sys.stdout.flush()
