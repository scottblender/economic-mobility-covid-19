import pandas as pd
from scipy.ndimage.measurements import label
data = pd.read_csv("/Users/scottblender/Desktop/longitudinal_compiled.csv") 
import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl
mpl.rcParams['figure.dpi'] = 200
# create a figure and axis
fig, ax = plt.subplots()
# plot for US
x = data['Dates'].astype(str)
y = data['avg_USA'].astype(float)
ax.plot(x,y, label="US")
# plt for PA
y_ = data['PA'].astype(float)
ax.plot(x,y_, label="PA")
# plt for NJ
y_ = data['NJ'].astype(float)
ax.plot(x,y_, label="NJ")
# plt for NY
y_ = data['NY'].astype(float)
ax.plot(x,y_, label="NY")
# plt for FL
y_ = data['FL'].astype(float)
ax.plot(x,y_, label="FL")
# plt for AL
y_ = data['AL'].astype(float)
ax.plot(x,y_, label="AL")
# plt for CA
y_ = data['CA'].astype(float)
ax.plot(x,y_, label="CA")
# plt for WI
y_ = data['WI'].astype(float)
ax.plot(x,y_, label="WI")
# set a title and labels
ax.set_title('Average Social Mobility Index for United States since January 1st, 2019')
ax.set_xlabel('Dates')
ax.set_ylabel('Social Mobility Index')
plt.legend(loc="upper right")
plt.xticks(np.arange(0, len(x)+1, 15))
plt.show()