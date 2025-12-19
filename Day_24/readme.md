# \## Day 24 — JSON \& DateTime (Python for Data Analytics)



\### Topics Covered

\- Writing Python data to JSON files using `json.dump()`

\- Reading JSON files using `json.load()`

\- Understanding data shapes used in analytics (list of dictionaries)

\- Calculating simple metrics from JSON data

\- Working with `datetime.now()`

\- Formatting dates and extracting year, month, and day



\### Key Learning

Today focused on how real-world data is stored and processed in analytics workflows. JSON is commonly used in APIs and data pipelines, while datetime handling is essential for reporting, filtering, and trend analysis.



This day builds a strong foundation for working with Pandas and time-based datasets.





**#Task 1 — Write JSON**

import json

student={

&nbsp;   "Name" : "Rafsan",

&nbsp;   "ID": 256987,

&nbsp;   "Department": "Data",

&nbsp;   "scores":\[10,20,45]

}

with open("student.json","w",newline='') as f:

&nbsp;print(json.dump(student,f))







 **#Task 2 — Read JSON**

import json 

with open("student.json","r") as f:

&nbsp;   file=json.load(f)

&nbsp;   average=sum(file\["scores"])/len(file\["scores"])

&nbsp;   print(file\["Name"])

&nbsp;   print(average)







**#Task\_3 Current Date**

from datetime import datetime

now=datetime.now()

print(now.date())







**#Task 4 — Date Parts**

\#From current datetime, print:Year:Month:Day:

from datetime import datetime 

now=datetime.now()

year=datetime.now().year

month=now.month

day=now.day

print(now.year)

print(f"year : {year}")

print(f"Month :{month}")

print(f"Day :{day}")







**#Task 5 — Sales JSON mini task**

import json 

sales=\[

&nbsp;   {"Rafsan":{"item":\["orange","apple"],"price":120,"date":"19-12-2025"}},

&nbsp;   {"Xess":{"item":\["apple","banana"],"price":80,"date":"19-12-2025"}},

&nbsp;   {"Xenifer":{"item":"fish","price":\[20],"date":"19-12-2025"}}

]

with open ("sales.json","w",newline="") as f :

&nbsp;   writer=json.dump(sales,f)

with open ("sales.json","r") as f:

&nbsp;   reader=json.load(f)

&nbsp;   print(reader)

