import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
data=pd.read_csv('CaseStudy.csv')
df=pd.DataFrame(data)
x=np.array(df['Month'])
y=np.array(df['Total Profit'])
plt.xlabel('Month')
plt.ylabel('Total Profit')
plt.title('Company Profit Per Month')
plt.plot(x,y,'o',linestyle='dashed',color='red',mfc='red')
plt.show()