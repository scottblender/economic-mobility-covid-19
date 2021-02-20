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
fig, (ax1, ax2, ax3, ax4, ax5, ax6, ax7) = plt.subplots(7, 1, sharex=True, sharey=True)
#plot for US Retail Mobility
ax1.plot(df_date, df_retail, color = "darkcyan", label = 'Retail')
ax1.set_title('US Mobility Changes since February 15th, 2020')
ax1.legend(prop={'size': 5})
#plot for US Grocery Mobility
ax2.plot(df_date, df_grocery, color ="darkslategray", label = 'Grocery')
ax2.legend(prop={'size': 5})
#plot for US Parks Mobility
ax3.plot(df_date, df_parks, color = "teal", label = 'Parks')
ax3.legend(prop={'size': 5})
#plot for US Transit Mobility
ax4.plot(df_date, df_transit, color = "dimgrey", label = 'Transit')
ax4.legend(prop={'size': 5})
ax4.set_ylabel("% Change in Mobility")
#plot for US Wokplaces Mobility
ax5.plot(df_date, df_workplaces, color = "mediumaquamarine", label = 'Workplace')
ax5.legend(prop={'size': 5})
#plot for US Residential Mobility
ax6.plot(df_date, df_residential, color = "cadetblue", label = 'Residential')
ax6.legend(prop={'size': 5})
#plot for US Avg Mobility
ax7.plot(df_date, df_mobility_avg, color = "darkcyan", label = 'Average Mobility')
ax7.legend(prop={'size': 5})
ax7.set_xlabel('Dates')
# set a title and labels
plt.xticks(np.arange(0, len(df_date)+1, 50))
plt.show()
