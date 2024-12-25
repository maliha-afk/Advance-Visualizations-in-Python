import matplotlib.pyplot as plt
import seaborn as sb
import pandas as pd
import numpy as np

weatherdf=pd.read_csv("weatherHistory.csv")

#print(weatherdf.info())

#plt.figure(figsize=(8,6))
#sb.barplot(y="Temperature (C)",x="Precip Type",data=weatherdf)
#plt.show()


#plt.figure(figsize=(8,6))
#sb.lineplot(x="Temperature (C)",y="Pressure (millibars)",data=weatherdf)
#plt.show()

plt.figure(figsize=(8,6))
sb.boxplot(x="Precip Type",y="Visibility (km)",data=weatherdf)
plt.show()