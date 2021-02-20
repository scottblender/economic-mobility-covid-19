import pandas as pd
import numpy as np
data = pd.read_csv("/Users/scottblender/Desktop/Data/US_Mobility_Report_Feb_2021.csv") 
data2 = pd.read_csv("/Users/scottblender/Desktop/Data/US_OWID_data.csv")
#load dataframes into pandas
df_date = data['date']
df_mobility_avg = data['mobility_average_percentage']
df_cases = data2['total_cases']
#imports
import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl
mpl.rcParams['figure.dpi'] = 200
# create a figure and axis
fig, ax = plt.subplots()
#plot for US Avg Mobility
ax.plot(df_date, df_mobility_avg, color = "darkcyan", label = 'Average Mobility')

ax1 = ax.twinx()
#plot for US COVID-19 Cases
ax1.plot(df_date, np.log10(df_cases), color="blue", label = 'Total Cases')
ax1.set_ylabel('Log(Cumulative COVID-19 Cases)')
# set a title and labels
ax.set_xlabel('Dates')
ax.set_ylabel('% Change in Mobility')
ax.set_title('Log(Cumulative COVID-19 Cases) and Mobility Changes')
ax.legend(prop={'size': 5})
plt.xticks(np.arange(0, len(df_date)+1, 50))
plt.show()

