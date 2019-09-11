import matplotlib.pyplot as plt
import csv
import pandas as pd

csv_file = pd.read_csv('test.csv')
csv_file=csv_file.ix[0:,['Number of Pass students','Number of Students']]
csv_file=csv_file.set_index(['Number of Pass students'])



csv_file.plot(color='Green')
plt.show()
