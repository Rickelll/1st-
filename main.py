import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

stores_dataset = pd.read_csv("stores data-set (1).csv")
print(stores_dataset)
print("Stores Dataset Columns: ", stores_dataset.columns)

sales_dataset = pd.read_csv("sales data-set.csv")
print(sales_dataset)
print("Sales Dataset Columns: ", sales_dataset.columns)

features_dataset = pd.read_csv("Features data set.csv")
print(features_dataset)
print("Features Dataset Columns: ", features_dataset.columns)

dataset = pd.merge(features_dataset, sales_dataset, how='left', on=['Store', 'Date', 'IsHoliday'])      #Merging all Dataset To make Data Easier to Manipulate
dataset = pd.merge(dataset, stores_dataset, how='left', on=['Store'])
print(dataset)