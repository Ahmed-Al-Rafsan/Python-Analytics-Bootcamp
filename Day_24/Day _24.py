#Task 1 — Write JSON
import json
student={
    "Name" : "Rafsan",
    "ID": 256987,
    "Department": "Data",
    "scores":[10,20,45]
}
with open("student.json","w",newline='') as f:
 print(json.dump(student,f))


 #Task 2 — Read JSON
import json 
with open("student.json","r") as f:
    file=json.load(f)
    average=sum(file["scores"])/len(file["scores"])
    print(file["Name"])
    print(average)

#Task_3 Current Date
from datetime import datetime
now=datetime.now()
print(now.date())

#Task 4 — Date Parts
#rom current datetime, print:Year:Month:Day:
from datetime import datetime 
now=datetime.now()
year=datetime.now().year
month=now.month
day=now.day
print(now.year)
print(f"year : {year}")
print(f"Month :{month}")
print(f"Day :{day}")

#Task 5 — Sales JSON mini task
import json 
sales=[
    {"Rafsan":{"item":["orange","apple"],"price":120,"date":"19-12-2025"}},
    {"Xess":{"item":["apple","banana"],"price":80,"date":"19-12-2025"}},
    {"Xenifer":{"item":"fish","price":[20],"date":"19-12-2025"}}
]
with open ("sales.json","w",newline="") as f :
    writer=json.dump(sales,f)
with open ("sales.json","r") as f:
    reader=json.load(f)
    print(reader)