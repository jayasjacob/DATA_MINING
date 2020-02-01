import pandas as pd
import numpy as np

import pyfpgrowth

df = pd.read_csv('dataset.csv', delimiter=',')

df = df.drop('ID', axis=1)

df = df.TRANSACTION

df=df.tolist()

print("Data Set :",df)

df = [line.split(',') for line in df]

print("Individual Items : ",df)

val=int(input("Enter the Minimum Support Count :"))
patterns = pyfpgrowth.find_frequent_patterns(df, val)

print("Expected patterns :",patterns)