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

#Merging all Dataset To make Data Easier to Manipulate
dataset = pd.merge(features_dataset, sales_dataset, how='left', on=['Store', 'Date', 'IsHoliday'])
dataset = pd.merge(dataset, stores_dataset, how='left', on=['Store'])
print(dataset)
print(dataset.describe())

#Checking NaN values of my columns to see which ones are useful
print(dataset.isnull().sum())

#Lots of these values are NaN and no record of anything over the weeks in the store so setting them as 0 is the best option
markdown_cols = ['MarkDown1','MarkDown2','MarkDown3','MarkDown4','MarkDown5']
dataset[markdown_cols] = dataset[markdown_cols].fillna(0)

#Only roughly 600 missing on CPI and Unemployment therefore enough data to be filled using median
dataset['CPI'].fillna(dataset['CPI'].median(), inplace=True)
dataset['Unemployment'].fillna(dataset['Unemployment'].median(), inplace=True)

#Getting rid of NaN values in Weekly Sales Column of my dataset
dataset['Weekly_Sales'].fillna(dataset['Weekly_Sales'].mean(), inplace=True)
print(dataset.isnull().sum())

pd.set_option('display.max_rows', None)
#Checking what type of data is NaN with Dept Column, The Majority of Data is Mean Therefore anywhere with Dept Column empty should be dropped
print(dataset[dataset['Dept'].isna()])

dataset = dataset.dropna(subset=['Dept'])
print(dataset[dataset['Dept'].isna()])

#Checking what values are in Column and Confirming they are a Boolean
print(dataset['IsHoliday'].unique())

#Changing boolean Values to integers 0 and 1
dataset['IsHoliday'] = dataset['IsHoliday'].astype(int)
print(dataset.head())

print(dataset.isnull().sum())
print("Dataset Columns: ", dataset.columns)
print(dataset.head())

#STEP - 2
#Finding the sales Difference between holidays and non-holidays weeks
#0 is false so they don't have a holiday
avg_weekly_sales_no_holidays = dataset[dataset['IsHoliday'] == 0]['Weekly_Sales'].mean()
print(f"Averager With No Holidays (Weekly Sales): {avg_weekly_sales_no_holidays}")

#1 is True so they do have a holiday
avg_weekly_sales_with_holidays = dataset[dataset['IsHoliday'] == 1]['Weekly_Sales'].mean()
print(f"Average With Holidays (Weekly Sales): {avg_weekly_sales_with_holidays}")

#STEP - 3
#Putting cleaned data into a DataFrame
cleaned_dataset = pd.DataFrame(dataset)
print(cleaned_dataset)

#STEP - 4
#Visualising Average Weekly Sales in a Chart
avg_sales_per_store = cleaned_dataset.groupby('Store')['Weekly_Sales'].mean().reset_index()
print("Average Weekly Sales per Store:")
print(avg_sales_per_store)

plt.figure(figsize=(16,6))
plt.bar(avg_sales_per_store['Store'], avg_sales_per_store['Weekly_Sales'])
plt.title("Average Weekly Sales per Store")
plt.xlabel("Store")
plt.ylabel("Average Weekly Sales")
plt.show()

print(cleaned_dataset.head())

#Formatting the date differently so that it does not run error in code
cleaned_dataset['Date'] = pd.to_datetime(cleaned_dataset['Date'], format='%d/%m/%Y')

stores_trend = cleaned_dataset.groupby(['Date','Store'])['Weekly_Sales'].sum().unstack()
plt.figure(figsize=(16,6))
plt.plot(stores_trend)
plt.title("Weekly Trend Over Time by Store")
plt.xlabel("Date")
plt.ylabel("Weekly Trend")
plt.show()

markdown_impact = cleaned_dataset.groupby(['IsHoliday'])[markdown_cols].sum()
markdown_impact.index = markdown_impact.index.map({0: "False", 1: "True"})
markdown_impact.plot(kind='bar', figsize=(12,6))
plt.title("Total Markdowns: Holiday vs Non-Holiday")
plt.xlabel("Holidays vs Non-Holiday")
plt.ylabel("Markdown Value")
plt.xticks(rotation=0)
plt.show()

region_sales = cleaned_dataset.groupby('Type')['Weekly_Sales'].mean().sort_values(ascending=False)
region_sales.plot(kind='bar', figsize=(10,6))
plt.title("Average Weekly Sales by Store Type")
plt.ylabel("Average Weekly Sales")
plt.show()