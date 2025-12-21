# \# Day 29 — Pandas Datetime Analysis (Python for Data Analytics)



This day focuses on handling datetime data using Pandas and performing real-world, time-based analysis — a core skill for Data Analysts.



\## Topics Covered

\- Converting string dates to datetime using `pd.to\_datetime()`

\- Extracting Year and Month from date columns

\- Filtering records based on date conditions

\- Grouping data by month using `groupby()`

\- Calculating aggregated metrics (sum, max)

\- Identifying highest-performing time periods using `idxmax()`



\## Key Skills Demonstrated

\- Analyst-style thinking with time-series data

\- Boolean filtering on DataFrames

\- Group-by aggregation for business insights

\- Debugging Pandas errors using Python tracebacks



\## Example Use Case

Analyzing monthly order trends and identifying the month with the highest total orders — a common real-world business reporting scenario.



This work reflects practical Pandas usage aligned with Data Analyst responsibilities.







**#Task 1-Create a DataFrame with:Date,Orders,Extract Year \& Month**

import pandas as pd

data=pd.DataFrame(

&nbsp;   {"Date":\["10-02-2025","15-04-2025","27-07-2025","31-12-2025"],

&nbsp;    "Orders":\[250,120,144,570]

&nbsp;   }

)

data\["Date"]=pd.to\_datetime(data\["Date"],dayfirst=True)

data\["Month"]=data\["Date"].dt.month

data\["Year"]=data\["Date"].dt.year

print(data)







**#Task 2 - Filter only records after a given date**

import pandas as pd

data=pd.DataFrame(

&nbsp;   {"Date":\["10-02-2025","15-04-2025","27-07-2025","31-12-2025"],

&nbsp;    "Orders":\[250,120,144,570]

&nbsp;   }

)

data\["Date"]=pd.to\_datetime(data\["Date"],dayfirst=True)

filter\_date=data\[data\["Date"]>="2025-05-01"]

print(filter\_date)









**#Task 3 (Analyst Thinking)-Calculate total orders per month**

import pandas as pd

data=pd.DataFrame(

&nbsp;   {"Date":\["10-02-2025","15-04-2025","27-07-2025","31-12-2025"],

&nbsp;    "Orders":\[250,120,144,570]

&nbsp;   }

)

data\["Date"]=pd.to\_datetime(data\["Date"],dayfirst=True)

data\["Month"]=data\["Date"].dt.month

total\_orders=data.groupby("Month")\["Orders"].sum()

print(total\_orders)







**#Task 4 - Find which month has the highest total orders**

import pandas as pd

data=pd.DataFrame(

&nbsp;   {"Date":\["10-02-2025","15-04-2025","27-07-2025","31-12-2025"],

&nbsp;    "Orders":\[250,120,144,570]

&nbsp;   }

)

data\["Date"]=pd.to\_datetime(data\["Date"],dayfirst=True)

data\["Month"]=data\["Date"].dt.month

monthly\_total=data.groupby("Month")\["Orders"].sum()

highest\_month=monthly\_total.idxmax()

highest\_orders=monthly\_total.max()

print(f"The highest selling month is {highest\_month} and highest\_orserd amount is {highest\_orders}")

