
import matplotlib
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import metrics


dataset = pd.read_csv('Absenteeism_at_work.csv',delimiter=';')

print(dataset.shape)
print(dataset.head())

X = dataset.drop('Age', axis=1)
y = dataset['Age']


from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20)


from sklearn.tree import DecisionTreeClassifier
classifier = DecisionTreeClassifier()
classifier.fit(X_train, y_train)


y_pred = classifier.predict(X_test)

print("Accuracy:",metrics.accuracy_score(y_test, y_pred))


from sklearn.metrics import classification_report, confusion_matrix
print(confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred))