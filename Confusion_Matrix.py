import pandas as pd
data=pd.read_csv('cancer_data.csv')
#print(data.head())
X=pd.DataFrame(data.iloc[:,:-1])
Y=pd.DataFrame(data.iloc[:,-1])
from sklearn.model_selection import train_test_split

from sklearn.metrics import confusion_matrix
y_actu = [2, 0, 2, 2, 0, 1, 1, 2, 2, 0, 1, 2]
y_pred = [0, 0, 2, 1, 0, 2, 1, 0, 2, 0, 2, 2]
q=confusion_matrix(y_actu, y_pred)
print(q)