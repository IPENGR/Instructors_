#Scatter Plot
#we will use "Duration" for the x-axis and "Calories" for the y-axis.
#Include the x and y arguments like this
#x = 'Duration', y = 'Calories'

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data2.csv')

df.plot(kind = 'scatter', x = 'Duration', y = 'Calories')

plt.show()