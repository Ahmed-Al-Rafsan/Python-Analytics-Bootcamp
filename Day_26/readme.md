# \# Python Bootcamp – Day 26: Pandas Introduction for Data Analytics



**## 📌 Overview**

Day 26 marks the beginning of my \*\*Data Analytics phase\*\* using Python.  

In this session, I learned the fundamentals of \*\*Pandas\*\*, the most important library for data analysis in Python.



This day focused on understanding how analysts work with structured data, CSV files, and DataFrames.



---



\## 🛠 Topics Covered

\- Introduction to Pandas

\- Creating Pandas DataFrames

\- Loading real-world CSV datasets

\- Basic data exploration techniques

\- Understanding rows, columns, and data types



---



\## 📊 Key Pandas Operations Practiced

\- `pd.DataFrame()`

\- `pd.read\_csv()`

\- `df.head()`

\- `df.shape`

\- `df.columns`

\- `df.info()`

\- Column selection using `loc` and `iloc`



---



\## 🎯 Learning Outcome

This day helped me transition from \*\*basic Python programming\*\* to \*\*data-focused thinking\*\*, which is essential for Data Analyst roles.



---



\## 📁 Files Included

\- `pandas\_intro.py`

\- `retail\_sales\_dataset.csv`



---



📈 This repository is part of my structured journey toward becoming a \*\*Data Analyst\*\*, followed by \*\*Data Engineering and AI Engineering\*\*.





**#Task 1 — Create DataFrame**

import pandas as pd

data={"Name":\["Rafsan","Emily","Cris","Tony"],

&nbsp;     "Age":\[32,22,25,30],

&nbsp;     "Country":\["Bangladesh","France","Australia","UAE"]

}

df=pd.DataFrame(data)

print(df)







**#Task 2 — CSV Loading -Load a CSV file using Pandas and print: First 5 rows,Shape,Column names**

import pandas as pd 

df=pd.read\_csv(r"C:\\Users\\ahmed\\Downloads\\retail\_sales\_dataset.csv")

print(df.head(5))

print(df.shape)

print(df.columns)







**#Task 3 — Exploration- Using the same DataFrame:Use info(),Identify:Total rows,Total columns,Data types**

import pandas as pd 

df=pd.read\_csv(r"C:\\Users\\ahmed\\Downloads\\retail\_sales\_dataset.csv")

\#print(df)

print(df.info())

print(df.columns)

print(f"Total columns:{df.shape\[1]}")

print(f"Total rows:{df.shape\[0]}")









**#Task 4 — Column Access-Print only one column from your DataFrame.**

import pandas as pd 

data={"Name":\["Rafsan","Emily","Cris","Tony"],

&nbsp;     "Age":\[32,22,25,30],

&nbsp;     "Country":\["Bangladesh","France","Australia","UAE"]

}

df=pd.DataFrame (data)

print(df.iloc\[:,1])

print(df.loc\[:,"Name"])

print(df.iloc\[2])

