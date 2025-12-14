# Day\_18



**#Task 1: Safe Average**

numbers=\[]

while True:

&nbsp;   try:

&nbsp;       user=int(input("Please insert numbers and press 0 to calculate: "))

&nbsp;       if user==0:

&nbsp;           break

&nbsp;       else:

&nbsp;           numbers.append(user)

&nbsp;   except:

&nbsp;       ValueError

&nbsp;       print("Please insert numbers only")

if len(numbers) >0:

&nbsp;   average=sum(numbers)/len(numbers)

&nbsp;   print(f"Average:{average}")





**#Task 2: Dictionary Lookup (Safe \& Clean)**

marks={"science":85,

&nbsp;      "english":98,

&nbsp;      "math":77}

try:

&nbsp;   user=input("please insert the subject name: ")

&nbsp;   print(f"{user} :{marks\[user]}")

except KeyError:

&nbsp;   print("inserted subject doesn't exist")

&nbsp; 



  **#Task 3: File Reading Protection**

try:

&nbsp;   import csv

&nbsp;   with open ("employees.csv","r") as f :

&nbsp;       reader=csv.reader(f)

&nbsp;       for i in reader:

&nbsp;           print(i)

except FileNotFoundError:

&nbsp;   print("file doesn't exist")



**#Task 4: Combined Error Handling**

try:

&nbsp;   user\_1=int(input("Please insert the first number:"))

&nbsp;   user\_2=int(input("Please insert the second number:"))

&nbsp;   number=user\_1/user\_2

&nbsp;   print(number)

except ValueError:

&nbsp;   print("please insert the number only")

except ZeroDivisionError:

&nbsp;   print("please use a correct divider apart from 0")



