import sys
print('Python: {}'.format(sys.version))
import numpy
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import warnings

dataset = pd.read_csv('Iris.csv')
print(dataset.head(20))
df=pd.DataFrame(dataset)
a=df.SepalLengthCm
b=df.PetalLengthCm
ax=sns.barplot(a,b)
plt.show()
