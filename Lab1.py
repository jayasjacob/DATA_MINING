import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2

data=pd.read_csv("diabetes.csv")
data.head()
print("Data From the Data set")
print(data)

#we can see that there are missing values in OUTCOME column

arr=['Pregnancy','Plas','Pressure','Skin','Test', 'Mass', 'pedi', 'Age', 'Class']
df=pd.read_csv('diabetes.csv')

#DataFrame object to a NumPy array to achieve faster computation. Also, let's segregate
# the data into separate variables so that the features and the labels are separated.
array=df.values
X = array[:,0:8]
Y = array[:,8]
# Feature extraction
test = SelectKBest(score_func=chi2, k=4)
fit = test.fit(X, Y)

# Summarize scores
np.set_printoptions(precision=3)
print(fit.scores_)

features = fit.transform(X)
# Summarize selected features
print(features[0:5,:])

#You can see the scores for each attribute and the 4 attributes chosen (those with the
# highest scores): plas, test, mass, and age. This scores will help you further in determining
# the best features for training your model.