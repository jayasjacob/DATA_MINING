import pandas as pd
import numpy as np
import statistics

# reading the file and selecting the coloum named "BMI"
filename = "diabetes.csv"
data = pd.read_csv(filename)
col_1 = data.BMI

# creating array
array = np.array(col_1)

# sort the array
array = np.sort(array)

# create bins
bin1 = np.zeros((30, 5))
bin2 = np.zeros((30, 5))

# Bin mean
for i in range(0, 150, 5):
    k = int(i / 5)
    mean = (array[i] + array[i + 1] + array[i + 2] + array[i + 3] + array[i + 4]) / 5
    for j in range(5):
        bin1[k, j] = mean
print("Bin Mean: \n", bin1)


# Bin boundaries
for i in range(0, 150, 5):
    k = int(i / 5)
    for j in range(5):
        if (array[i + j] - array[i]) < (array[i + 4] - array[i + j]):
            bin2[k, j] = array[i]
        else:
            bin2[k, j] = array[i + 4]
print("Bin Boundaries: \n", bin2)