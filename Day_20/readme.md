# **Day 20 ( Mini Project) :**



Mini Project: Salary Analytics Tool


**Project Overview**



This mini project demonstrates how Python can be used for basic data analytics tasks without external libraries. The script reads salary data from a CSV file and calculates key statistics using reusable functions.




**Concepts Practiced**



CSV file handling



Function design \& parameters



Data flow between functions



Avoiding global variable dependency



Using if \_\_name\_\_ == "\_\_main\_\_" for safe execution



**Writing reusable Python modules**

import csv

def read\_salaries():

&nbsp;   with open ("data.csv","r") as f :

&nbsp;       reader=csv.reader(f)

&nbsp;       next(reader)

&nbsp;       salaries=\[]

&nbsp;       for i in reader:

&nbsp;           salaries.append((int(i\[2])))

&nbsp;       return salaries

salaries=read\_salaries()

def average\_salary(salaries):

&nbsp;   return round(sum(salaries)/len(salaries))

def highest\_salary(salaries):

&nbsp;   return max(salaries)

def minimum\_salary(salaries):

&nbsp;   return min(salaries)

if \_\_name\_\_=="\_\_main\_\_":

&nbsp;   print(f'Salary:{salaries}')

&nbsp;   print(f"Average Salary: {average\_salary(salaries)}")

&nbsp;   print(f"Maximum Salary : {highest\_salary(salaries)}")

&nbsp;   print(f"Minimum Salary : {minimum\_salary(salaries)}")

&nbsp;       

&nbsp;      

&nbsp;

&nbsp;       

