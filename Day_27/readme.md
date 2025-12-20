# \# Day 27 — Pandas GroupBy \& Aggregation (Data Analytics)



**## Overview**

Day 27 focuses on one of the most important skills for Data Analysts: 

using Pandas `groupby()` and aggregation functions to answer business questions.



This day simulates real-world analytical tasks such as calculating total sales,

average sales, and transaction counts across categories and regions.



---



**## Topics Covered**

\- Pandas `groupby()` basics

\- Aggregation functions: `sum()`, `mean()`, `count()`

\- Grouping by single column

\- Grouping by multiple columns (Category + Region)

\- Multiple aggregations using `.agg()`

\- Business-focused data interpretation



---



\## Sample Dataset

```python

Category | Region | Sales





**#Task 1 — Total Sales by Category**

import pandas as pd



data = {

&nbsp;   "Category": \["Electronics", "Electronics", "Clothing", "Clothing", "Furniture"],

&nbsp;   "Region": \["East", "West", "East", "West", "East"],

&nbsp;   "Sales": \[1200, 900, 500, 700, 400]

}



df = pd.DataFrame(data)

result=df.groupby("Category")\["Sales"].sum()

print(result)





**#Task 2 — Average Sales by Category**

import pandas as pd 

data = {

&nbsp;   "Category": \["Electronics", "Electronics", "Clothing", "Clothing", "Furniture"],

&nbsp;   "Region": \["East", "West", "East", "West", "East"],

&nbsp;   "Sales": \[1200, 900, 500, 700, 400]

}

df=pd.DataFrame(data)

result=df.groupby("Category")\["Sales"].mean()

print(result)



**#Task 3 — Total Sales by Region**

import pandas as pd 

data = {

&nbsp;   "Category": \["Electronics", "Electronics", "Clothing", "Clothing", "Furniture"],

&nbsp;   "Region": \["East", "West", "East", "West", "East"],

&nbsp;   "Sales": \[1200, 900, 500, 700, 400]

}

df=pd.DataFrame(data)

result=df.groupby( "Region")\["Sales"].sum()

print(result)





**#Task 4 — Category + Region - Find total sales grouped by BOTH Category and Region**

import pandas as pd 

data = {

&nbsp;   "Category": \["Electronics", "Electronics", "Clothing", "Clothing", "Furniture"],

&nbsp;   "Region": \["East", "West", "East", "West", "East"],

&nbsp;   "Sales": \[1200, 900, 500, 700, 400]

}

df=pd.DataFrame(data)

result=df.groupby(\["Category","Region"])\["Sales"].sum()

print(result)





**#Task 5 — Multiple Aggregations -For each Category, calculate:Total Sales,Average Sales,Number of transactions**

import pandas as pd

data = {

&nbsp;   "Category": \["Electronics", "Electronics", "Clothing", "Clothing", "Furniture"],

&nbsp;   "Region": \["East", "West", "East", "West", "East"],

&nbsp;   "Sales": \[1200, 900, 500, 700, 400]

}

df=pd.DataFrame(data)

Total\_Sales=df.groupby("Category")\["Sales"].sum()

print(f"Total\_Sales= {Total\_Sales}")

print(f"Average Sales= {df.groupby("Category")\["Sales"].mean()}")

print(f"Total Number of Transaction = {df.groupby("Category")\['Sales'].count()}")

