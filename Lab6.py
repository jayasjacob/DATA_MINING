import pandas as pd
import numpy as np

import pyfpgrowth

df = pd.read_csv('dataset.csv', delimiter=';')

df = df.drop('ID', axis=1)

df = df.TRANSACTION

df=df.tolist()

print(df)

df = [line.split(',') for line in df]

print(df)

patterns = pyfpgrowth.find_frequent_patterns(df, 2)

print(patterns)


# transactions = [[1, 2, 5],
#                 [2, 4],
#                 [2, 3],
#                 [1, 2, 4],
#                 [1, 3],
#                 [2, 3],
#                 [1, 3],
#                 [1, 2, 3, 5],
#                 [1, 2, 3]]
#
# print(transactions)
#
# patterns = pyfpgrowth.find_frequent_patterns(transactions, 2)
#
# print(patterns)


# import pandas as pd
# import numpy as np
# import pyfpgrowth
#
# df = pd.read_csv('GroceryStoreDataSet.csv')
#
#
# Products_list = df.values.tolist()
# #print(Products_list)
#
# patterns = pyfpgrowth.find_frequent_patterns(Products_list,2)
#
# print(patterns)