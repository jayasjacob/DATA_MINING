"""

write a menue driven program for implementing the data transformation with respect to any dataset

"""

import pandas as pd
import numpy as np
import statistics

# reading the file
filename = "diabetes.csv"
data = pd.read_csv(filename)
col_1 = data.BMI
array = np.array(col_1)


# min max normalization
def Min_Max():
    print("MIN MAX Normalization")
    new_min = float(input("ENTER THE NEW MINIMUM VALUE :"))
    new_max = float(input("ENTER THE NEW MAXIMUM VALUE "))
    mn = float(min(array))
    mx = float(max(array))

    for val in array:
        v = float((((val - mn) / (mx - mn)) * (new_max - new_min)) + new_min)
        print("Result :", v)
    return


def Z_Score():
    print("Z Score Normalization")
    mean= statistics.mean(array)
    standrddeviation = statistics.stdev(array)

    for val in array:
        v=float((val-mean)/standrddeviation)
        print("Result :", v)
    return


def Decimal_Scaling():
    print("Decimal Scaling")

    for val in array:
        v=float(val/100)
        print("Result :",v)
    return


# menue
def main():
    print("Menue")
    print("1. MIN MAX Normalization")
    print("2. Z-Score Normalization")
    print("3. Decimal Scaling Normalization")
    num = input("Choose an option :")

    # switch
    num = int(num)

    if (num == 1):
        Min_Max()
    elif (num == 2):
        Z_Score()
    elif (num == 3):
        Decimal_Scaling()
    else:
        print("Invalid Entry")


for i in range(0, 10, 1):
    main()