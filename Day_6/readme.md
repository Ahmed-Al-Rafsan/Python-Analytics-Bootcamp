# **Day - 6 :**



\##Task 1 — Clean the Price List

products = \["$5.50", "$12.99", "$8.30", "$1.20"]

x=\[]

for i in products :

&nbsp;  x.append(float(i.replace("$","")))

print(x)







\#Task 2 — Count How Many Items Are Above 10 Dollars

products = \["$5.50", "$12.99", "$8.30", "$1.20","$13.20","$14.20"]

x=\[]

for i in products :

&nbsp;  x.append(float(i.replace("$","")))

while True:

&nbsp;  Total=0

&nbsp;  for item in x:

&nbsp;     if item >= 10 :

&nbsp;        Total +=1

&nbsp;  break

print(Total)









\#Task 3 — Format all floats to 2 decimal places

products = \["$5.50", "$12.99", "$8.30", "$1.20","$13.20","$14.20"]

x=\[]

for items in products :

&nbsp;   x.append(float(items.replace("$","")))

for value in x:

&nbsp;  print(f"{value:.2f}")







\#Task 4. Select only the values below 10

products = \["$5.50", "$12.99", "$8.30", "$1.20","$13.20","$14.20"]



x=list(((map(lambda p:float(p.replace("$","")),products))))

box=\[]

for i in x : 

&nbsp;   if i<10:

&nbsp;       box.append(i)

print(box)







\#Task 5 — Count Vowels \& Consonants in a Word (Correct Version)

\#This time, you must:

\#Ask the user for a word

\#Validate: only alphabets allowed

\#Count:

\#vowels

\#consonants

\#Print both numbers

\#Loop again if the user enters invalid input

\#Stop only when valid input is given

vowel=\[]

vowel\_count=0

consonent=\[]

consonent\_count=0

while True :

&nbsp;   user=(input("Please insert a Word :")).lower()

&nbsp;   if not user.isalpha():

&nbsp;       print("Only Alphabets are allowed , Please try a word!")

&nbsp;       continue

&nbsp;   for ch in user: 

&nbsp;     if ch in'aeiou':

&nbsp;       vowel.append(ch)

&nbsp;       vowel\_count +=1

&nbsp;     else:

&nbsp;       consonent.append(ch) 

&nbsp;       consonent\_count+=1

&nbsp;   break

print(f"Total Voewl {vowel\_count} and Vowels are: {vowel}")

print(f"Total consonent {consonent\_count} and consonent are: {consonent}")

&nbsp;  

&nbsp;  

