import pandas as pd
data = pd.read_csv("/Users/scottblender/Desktop/Data/US_Mobility_Report_Feb_2021.csv") 
#load dataframes into pandas
df_date = data['date']
df_retail = data['retail_and_recreation_percent_change_from_baseline']
df_grocery = data['grocery_and_pharmacy_percent_change_from_baseline']
df_parks = data['parks_percent_change_from_baseline']
df_transit = data['transit_stations_percent_change_from_baseline']
df_workplaces = data['workplaces_percent_change_from_baseline']
df_residential = data['residential_percent_change_from_baseline']
df_mobility_avg = data['mobility_average_percentage']
#imports
import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl
mpl.rcParams['figure.dpi'] = 200
# create a figure and axis
fig, ax = plt.subplots()
#plot for US Retail Mobility
ax.plot(df_date, df_retail, label = 'Retail')
#plot for US Grocery Mobility
ax.plot(df_date, df_grocery, label = 'Grocery')
#plot for US Parks Mobility
ax.plot(df_date, df_parks, label = 'Parks')
#plot for US Transit Mobility
ax.plot(df_date, df_transit, label = 'Transit')
#plot for US Wokplaces Mobility
ax.plot(df_date, df_workplaces, label = 'Workplace')
#plot for US Residential Mobility
ax.plot(df_date, df_residential, label = 'Residential')
#plot for US Avg Mobility
ax.plot(df_date, df_mobility_avg, label = 'Average Mobility')
# set a title and labels
ax.set_xlabel('Dates')
ax.legend(prop={'size': 5})
ax.set_ylabel("% Change in Mobility")
ax.set_title('US Mobility Changes since February 15th, 2020')
plt.xticks(np.arange(0, len(df_date)+1, 50))
plt.show()