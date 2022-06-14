import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
data=pd.read_csv('CaseStudy.csv')
col=list(data.columns)
y=[]
for i in col:
    if i!= 'Total Units' and i!='Total Profit' and i!='Month':
        y.append(data[i].sum())
yp=np.array(y)
lab=['Facecream','Facewash','Toothpaste','Bathing Soap','Shampoo','Moisturizer']
plt.pie(yp,labels=lab,autopct='%1.1f%%')
plt.title("Sales")
plt.axis("equal")
plt.legend()
plt.show()