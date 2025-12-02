import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#STEP - 1
#Load and Inspect Data

# Load datasets
stores_dataset = pd.read_csv("stores data-set (1).csv")
print(stores_dataset)
print("Stores Dataset Columns: ", stores_dataset.columns)


sales_dataset = pd.read_csv("sales data-set.csv")
print(sales_dataset)
print("Sales Dataset Columns: ", sales_dataset.columns)

features_dataset = pd.read_csv("Features data set.csv")
print(features_dataset)
print("Features Dataset Columns: ", features_dataset.columns)

# Merging all datasets into one main dataset

# Merge features with sales data
dataset = pd.merge(features_dataset, sales_dataset, how='left', on=['Store', 'Date', 'IsHoliday'])


# Merge store information
dataset = pd.merge(dataset, stores_dataset, how='left', on=['Store'])
print(dataset)
print(dataset.describe())

#Checking NaN values of my columns to see which ones are useful

print(dataset.isnull().sum())

# MarkDown values are missing for many weeks, replace with 0
markdown_cols = ['MarkDown1','MarkDown2','MarkDown3','MarkDown4','MarkDown5']
dataset[markdown_cols] = dataset[markdown_cols].fillna(0)

# CPI and Unemployment have few missing values, fill with median
dataset['CPI'].fillna(dataset['CPI'].median(), inplace=True)
dataset['Unemployment'].fillna(dataset['Unemployment'].median(), inplace=True)

# Weekly_Sales missing values, replace with mean
dataset['Weekly_Sales'].fillna(dataset['Weekly_Sales'].mean(), inplace=True)
print(dataset.isnull().sum())

pd.set_option('display.max_rows', None)

# Show rows where Dept is missing
print(dataset[dataset['Dept'].isna()])

# Remove rows with missing Dept values
dataset = dataset.dropna(subset=['Dept'])

# Confirm no missing Dept values remain
print(dataset[dataset['Dept'].isna()])

# Check values
print(dataset['IsHoliday'].unique())

# Convert boolean to 0 (Non-Holiday) and 1 (Holiday)
dataset['IsHoliday'] = dataset['IsHoliday'].astype(int)
print(dataset.head())

print(dataset.isnull().sum())
print("Dataset Columns: ", dataset.columns)
print(dataset.head())

#STEP - 2
# Compare Holiday vs Non-Holiday Sales

# Average weekly sales during non-holiday weeks
avg_weekly_sales_no_holidays = dataset[dataset['IsHoliday'] == 0]['Weekly_Sales'].mean()
print(f"Averager With No Holidays (Weekly Sales): {avg_weekly_sales_no_holidays}")

# Average weekly sales during holiday weeks
avg_weekly_sales_with_holidays = dataset[dataset['IsHoliday'] == 1]['Weekly_Sales'].mean()
print(f"Average With Holidays (Weekly Sales): {avg_weekly_sales_with_holidays}")

# STEP - 3

# Storing cleaned dataset
cleaned_dataset = pd.DataFrame(dataset)
print(cleaned_dataset)

#STEP - 4
# Visualising Average Weekly Sales in a bar chart
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

# Convert Date to datetime format to avoid plotting errors
cleaned_dataset['Date'] = pd.to_datetime(cleaned_dataset['Date'], format='%d/%m/%Y')

stores_trend = cleaned_dataset.groupby(['Date','Store'])['Weekly_Sales'].sum().unstack()
plt.figure(figsize=(16,6))
plt.plot(stores_trend)
plt.title("Weekly Trend Over Time by Store")
plt.xlabel("Date")
plt.ylabel("Weekly Trend")
plt.show()

# Markdown Impact: Holiday vs Non-Holiday

markdown_impact = cleaned_dataset.groupby(['IsHoliday'])[markdown_cols].sum()

# Rename index for readability
markdown_impact.index = markdown_impact.index.map({0: "Non-Holidays", 1: "Holidays"})

markdown_impact.plot(kind='bar', figsize=(12,6))
plt.title("Total Markdowns: Holiday vs Non-Holiday")
plt.xlabel("Holidays vs Non-Holiday")
plt.ylabel("Markdown Value")
plt.xticks(rotation=0)
plt.show()

# Average Weekly Sales by Store Type

region_sales = cleaned_dataset.groupby('Type')['Weekly_Sales'].mean().sort_values(ascending=False)
region_sales.plot(kind='bar', figsize=(10,6))
plt.title("Average Weekly Sales by Store Type")
plt.ylabel("Average Weekly Sales")
plt.xticks(rotation=0)
plt.show()