import pandas as pd
import numpy as np
data = pd.read_csv("/Users/scottblender/Desktop/Data/US_Mobility_Report_Feb_2021.csv") 
data2 = pd.read_csv("/Users/scottblender/Desktop/Data/US_OWID_data.csv")
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
#statistics
from scipy import stats
X = np.log10(df_cases)
Y = df_mobility_avg
slope, intercept, r_value, p_value, slope_std_error = stats.linregress(X,Y)
predict_y = slope *  + intercept
import seaborn as sns
sns.regplot(x=np.log10(df_cases), y=df_mobility_avg, fit_reg=True, logx=False, line_kws={'label':'$y=%3.7s*x+%3.7s$'%(slope, intercept)})
ax.set_xlabel('Log(Cumulative COVID-19 Cases)')
ax.set_ylabel('% Change in Mobility')
ax.set_title('Regression of Log(Cumulative COVID-19 Cases) and % Changes in Mobility')
ax.legend()
plt.show()