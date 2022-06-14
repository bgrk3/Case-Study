import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
data=pd.read_csv('CaseStudy.csv')
df=pd.DataFrame(data)
x=np.array(df['Month'])
y=np.array(df['Soap'])
plt.bar(x,y)
plt.grid(linestyle='dashed')
plt.xlabel('Month')
plt.ylabel('Sales of Soap')
plt.title('Soap Sales')
plt.show()