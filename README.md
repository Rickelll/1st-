# Retail Sales Data Analysis

This project has been made as part of a milestone project with the Data Analytic & AI course provided by Code Institute.
It demonstrates an end-to-end data workflow, including Extracting, Transforming and Loading (ETL) data, as well as data visualisation using descriptive, trend, impact and comparative analysis.

The project guides you step by step through the entire process, from data cleaning to feature engineering, clearly explaining each stage.

## Dataset Content

This Dataset is sourced from [kaggle.](https://www.kaggle.com/datasets/manjeetsingh/retaildataset)

The Project uses dataset sourced from Kaggle, consisting of three CSV files:
- *Stores Dataset- Stores Number of Store, Types and Size of Store*
- *Sales Dataset- Weekly Sales data by Store, Department and Date*
- *Features Dataset- External Store data such as Holidays, CPI and Markdown*
    - *Date*
    - *Type of Store*
    - *Department of Store*
    - *Holiday indicator*
    - *CPI*
    - *Unemployment*
    - *Markdwon 1-5*
    - *Weekly Sales*

## Dataset Characteristics
- *45 stores*
- *Multiple departments*
- *Varying date ranges per store*
- *Contains missing values*
- *Covers January 2010 to October 2012*
- *Contains missing values that require cleaning and preprocessing*

## Agile Methodology
- *In the beginning of the project I decided to create Kanban project, to keep track of progression. The idea is to help me in following a direction while building this project.*
-  *The Kanban Table Project can be found [here.](https://github.com/users/Rickelll/projects/8/views/1)*

## Business Requirements
The ultimate goal is to understand how our holidays, store types and time impact each of our stores performances, Finding this insight on our data can lead to better business strategies as well as better management across all of our stores.

The core business questions addressed by this project are:
1. What are our busiest times of the year?
2. How do sales trends evolve over time across different stores?
3. Are there differences in performance between stores and store types?
4. Do markdowns differ between holiday and non-holiday weeks?

## Hypothesis and Validation

1. Hypotheses:
- *Average weekly sales differ between stores*
- *Sales trends change based on the time of year*
- *Markdown activity is higher during holiday weeks than during non-holiday weeks*
- *Different store types may vary in size leading to differences in sales volume*

## Validation Methods

2. Validation Methods:
- *We consider that stores differ in their average weekly sales performance.*
  - *A comparison of average weekly sales across all stores can help in investigating if this is true.*
- *We consider that weekly sales trends change over time and differ across stores, reflecting store-specific and seasonal patterns.*
  - *A trend analysis of weekly sales over time for each store can help in investigating if this is true.*
- *We consider that markdown promotional activity is higher during holiday weeks than during non-holiday weeks.*
  - *A comparison of total markdown values between holiday and non-holiday periods can help in investigating if this is true.*
- *We consider that store type influences sales performance, where stores of different types achieve different average weekly sales.*
 - *A comparison of average weekly sales across store types can help in investigating if this is true.*

## Data Cleaning and Analyst Techniques
# Techniques Used:
- *Dataset merging through pandas*
- *Null Value analysis*
- *mean and median used for missing values*
- *Feature Engineering on types of Data*
- *Feature grouping*

# Missing Data Handing Justification

---

|Column|Method| Reason                                                                                                                              |
|:----|:----|:------------------------------------------------------------------------------------------------------------------------------------|
|MarkDown1–5|Filled with 0| Missing values indicate no promotion; setting to 0 avoids issues in visual comparisons |
|CPI & Unemployment|Median| Median was chosen to avoid extreme values and keep a realistic visual comparsion |
|Weekly_Sales|Mean| This was done so rows were not removed and the overall sales picture stayed consistent |
|Dept|Rows removed| Without department information, it is unclear how to interpret the sales data, so these records were removed|


These decisions were made based on best practices taught during the course.

## Sales and Markdown Analysis
1. Average Weekly Sales per Store

![Average Weekly Sales](/images/Weekly Sales Bar Chart.png)

### Description:
- This bar chart represents the average weekly sales for each of the 45 stores in the dataset.