# Day\_17 



**#Practice Task: Read a CSV File**

import csv 

with open(r"C:\\Users\\ahmed\\OneDrive\\Documents\\Desktop\\Airline\_Delay\_Cause.csv","r") as f :

&nbsp;   file=csv.reader(f)

&nbsp;   for i in range(20):

&nbsp;       print(next(file))







**#Task 1 \& 2 — Create CSV**

import csv



\#writting first

with open("employees.csv","w",newline="") as f :

&nbsp;   writer=csv.writer(f)

&nbsp;   writer.writerow(\["id","name","department","salary"])

&nbsp;   writer.writerow(\[1,"Rafsan","Data",5000])

&nbsp;   writer.writerow(\[2,"Alex","HR",4000])

&nbsp;   writer.writerow(\[3,"Jess","IT",5500])



\#reading the created csv:

with open("employees.csv","r") as f :

&nbsp;   reader=csv.reader(f)

&nbsp;   for i in reader:

&nbsp;       print(i)       





**#Task 3 — Skip Header**

import csv 



\#writing/creating csv without Header

with open("employees.csv","w",newline="") as f :

&nbsp;   x=csv.writer(f)

&nbsp;   x.writerow(\["Id",'Name',"Designation","Salary"])

&nbsp;   x.writerow(\[101,"Rafsan","Ai Engineer",5000000])

&nbsp;   x.writerow(\[105,"Alex","Data Analyst",5222635])

&nbsp;   x.writerow(\[107,"Xessi","Data Scientist",452221])



\#reading for checking purposes

with open("employees.csv","r") as f :

&nbsp;   y=csv.reader(f)

&nbsp;   next(y)

&nbsp;   for i in y:

&nbsp;       print(i)





**#Task 4: Salary Sum**



\#writing/creating csv without Header

with open("employees.csv","w",newline="") as f :

&nbsp;   x=csv.writer(f)

&nbsp;   x.writerow(\["Id",'Name',"Designation","Salary"])

&nbsp;   x.writerow(\[101,"Rafsan","Ai Engineer",5000000])

&nbsp;   x.writerow(\[105,"Alex","Data Analyst",5222635])

&nbsp;   x.writerow(\[107,"Xessi","Data Scientist",452221])



\#reading for checking purposes

with open("employees.csv","r") as f :

&nbsp;   y=csv.reader(f) 

&nbsp;   next(y)

&nbsp;   total=0

&nbsp;   for i in y:

&nbsp;       total+=int(i\[3])

print(f"Total Salary:{total}")





**#Task 5: Salary Sum**

import csv

\#writing/creating csv without Header

with open("employees.csv","w",newline="") as f :

&nbsp;   x=csv.writer(f)

&nbsp;   x.writerow(\["Id",'Name',"Designation","Salary"])

&nbsp;   x.writerow(\[101,"Rafsan","Ai Engineer",5000000])

&nbsp;   x.writerow(\[105,"Alex","Data Analyst",5222635])

&nbsp;   x.writerow(\[107,"Xessi","Data Scientist",452221])



\#reading for checking purposes

with open("employees.csv","r") as f :

&nbsp;   y=csv.reader(f) 

&nbsp;   next(y)

&nbsp;   total\_salary=\[]

&nbsp;   for i in y:

&nbsp;       total\_salary.append(int(i\[3]))

print(total\_salary)

print(f"Average Salary:{round(sum(total\_salary)/len(total\_salary))}")





**#Task 6: Salary Sum**

import csv

\#reading for checking purposes

with open("employees.csv","r") as f :

&nbsp;   y=csv.reader(f) 

&nbsp;   next(y)

&nbsp;   for i in y:

&nbsp;       salary=int(i\[3])

&nbsp;   if salary>45000000:

&nbsp;           print(i\[1])





**#Task 7 — Dictionary Reader**

import csv

with open ("employees.csv","r") as f :

&nbsp;   reader=csv.DictReader(f)

&nbsp;   for i in reader:

&nbsp;       print(f"Name:{i\['Name']} and Designation:{i\['Designation']}")





**#Task 8: Create a Filtered CSV File** 

import csv 

with open("employees.csv","r") as f ,open("high\_salary.csv","w",newline="") as d :

&nbsp;   reader=csv.DictReader(f)

&nbsp;   writer=csv.writer(d)

&nbsp;   writer.writerow(\["Id","Name","Designation","Salary"])

&nbsp;   for i in reader:

&nbsp;       Salary=int(i\["Salary"])

&nbsp;       if Salary >48000:

&nbsp;           writer.writerow(\[i\["Id"],i\["Name"],i\["Designation"],i\["Salary"]])





