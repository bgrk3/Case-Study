import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
data=pd.read_csv('CaseStudy.csv')
df=pd.DataFrame(data)
x=np.array(df['Month'])
y=np.array(df['Toothpaste'])
plt.xlabel('Month')
plt.ylabel('No. of Units Sold')
plt.title('Toothpaste Sales')
plt.scatter(x,y)
plt.grid(linestyle='dashed')
plt.show()