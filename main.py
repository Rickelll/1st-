import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#STEP - 1
#Cleaning the Dataset

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

print(dataset.describe())
print(dataset.isnull().sum())                               #Checking NaN values of my columns to see which ones are useful

dataset = dataset[['Store', 'Date', 'Temperature', 'Weekly_Sales', 'Dept', 'Size','IsHoliday']]             #Gets Relevant Columns for data
print(dataset.head())

print("Dataset Columns: ", dataset.columns)
print(dataset.isnull().sum())

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

print("Dataset Columns: ", dataset.columns)
print(dataset.describe())
print(dataset.isnull().sum())                               #Checking NaN values of my columns to see which ones are useful

dataset = dataset[['Store', 'Date', 'Temperature', 'Weekly_Sales', 'Dept', 'Size','IsHoliday']]
print(dataset.head())

print("Dataset Columns: ", dataset.columns)
print(dataset.isnull().sum())

dataset['Weekly_Sales'].fillna(dataset['Weekly_Sales'].mean(), inplace=True)                    #Getting rid of NaN values in Weekly Sales Column of my dataset
print(dataset.isnull().sum())

pd.set_option('display.max_rows', None)
print(dataset[dataset['Dept'].isna()])                                                          #Checking what type of data is NaN with Dept Column, Majority of Data is Mean Therefore anywhere with Dept Column empty should be dropped

dataset = dataset.dropna(subset=['Dept'])
print(dataset[dataset['Dept'].isna()])

print(dataset['IsHoliday'].unique())                                                            #Checking what values are in Column and Confirming they are a Boolean
dataset['IsHoliday'] = dataset['IsHoliday'].astype(int)                                         #Changing boolean Values to integers 0 and 1
print(dataset.head())

print(dataset.isnull().sum())
print("Dataset Columns: ", dataset.columns)
print(dataset.head())

#STEP - 2
#Finding the sales Difference between holidays and non-holidays weeks
avg_weekly_sales_no_holidays = dataset[dataset['IsHoliday'] == 0]['Weekly_Sales'].mean()                    #0 is false so they don't have a holiday
print(f"Averager With No Holidays (Weekly Sales): {avg_weekly_sales_no_holidays}")
avg_weekly_sales_with_holidays = dataset[dataset['IsHoliday'] == 1]['Weekly_Sales'].mean()                  #1 is True so they do have a holiday
print(f"Average With Holidays (Weekly Sales): {avg_weekly_sales_with_holidays}")

#STEP - 3
#Putting cleaned data into a DataFrame
cleaned_dataset = pd.DataFrame(dataset)
print(cleaned_dataset)