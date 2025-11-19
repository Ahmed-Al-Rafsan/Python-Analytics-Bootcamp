# **Day 7**



\#Print the total sum of only even numbers.

values = \[12, 5, 7, 18, 22, 9, 10]

x=\[]

for i in values :

&nbsp;   if i%2==0:

&nbsp;       x.append(i)

\# printing the sum of only total numbers 

total=sum(x)

print(total)

\#Task 2 :

\#Filter only the prices greater than 50

\#Increase each selected price by 10%

\#Store them in a new list

\#Print the final list with each value formatted to 2 decimals

prices = \[15.50, 99.99, 45.00, 120.30, 9.99, 230.50]

x=\[]

for i in prices : 

&nbsp;   if i > 50 :

&nbsp;       x.append(float(i\*0.1))

final=\[]

for k in x :

&nbsp;   final.append(f"{k:.2f}") 

print(final)



\#Task : Ask the user for a word

\#👉 Reverse it using a loop (no slicing, no shortcuts!)

\#👉 Print the reversed result



while True :

&nbsp;   user=(input("Please write a word: ")).lower()

&nbsp;   x=" "

&nbsp;   if not user.isalpha()==True:

&nbsp;       print("Please insert a word only !")

&nbsp;       continue 

&nbsp;   else: 

&nbsp;       for i in user :

&nbsp;           x=i+x

&nbsp;       break

print(x)





\#👉 Ask the user for a sentence

\#👉 Count how many uppercase letters

\#👉 Count how many lowercase letters

\#👉 Print both numbers

\#👉 Ignore spaces and punctuation (Python automatically handles this)

upper=0

upper\_letter =""



lower=0

lower\_letter=''



while True:

&nbsp;   user=input("Please write a sentence : ")

&nbsp;   valid =True 

&nbsp;   for i in user:

&nbsp;       if not i.isalpha() and i != " ":

&nbsp;           valid = False 

&nbsp;           break

&nbsp;   if not valid : 

&nbsp;       print("Please Write A Sentence Only! ")

&nbsp;       continue

&nbsp;   for i in user :

&nbsp;       if i.isupper():

&nbsp;               upper\_letter+=i

&nbsp;               upper+=1

&nbsp;       elif i.islower():

&nbsp;           lower\_letter+=i

&nbsp;           lower+=1

&nbsp;   break 

print(f"The Upper Letters are {upper\_letter} which is Toatal {upper}")

print(f"The Lower Letters are {lower\_letter} which is Toatal {lower}")

