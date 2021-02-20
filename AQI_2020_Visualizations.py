#imports
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
#filtering for only PM2.5
airData = pd.read_csv("/Users/scottblender/Desktop/Data/daily_aqi_by_county_2020.csv")
airData = airData[airData['Defining Parameter'] == 'PM2.5']
print(airData.head())
#grouping AQI by state for analysis
avgData = airData.groupby('State', as_index=False).mean()
print(avgData.head())
#average mobility over time
mobilitydata = pd.read_csv("/Users/scottblender/Desktop/Data/longitudinal_state_only_compiled.csv") 
mobilitydata = mobilitydata.mean()
print(mobilitydata.head())
#set dataframes
df_mobility = mobilitydata
df_aqi = avgData['AQI']
#statistics
from scipy import stats
X = df_aqi
Y = df_mobility
slope, intercept, r_value, p_value, slope_std_error = stats.linregress(X,Y)
predict_y = slope *  + intercept
# create a figure and axis
fig, ax = plt.subplots()
#visualization
sns.regplot(x = df_aqi, y=df_mobility, fit_reg=True, logx=False, line_kws={'label':'$y=%3.7s*x+%3.7s$'%(slope, intercept)})
ax.set_xlabel('Mean AQI (2020)')
ax.set_ylabel('Social Mobility Index')
ax.set_title('Regression of AQI and Mobility Index')
ax.legend()
plt.show()




