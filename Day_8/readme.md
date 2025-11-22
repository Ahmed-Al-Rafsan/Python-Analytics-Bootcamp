

# **Day 8 :**

\#Task — Create a function that calculates the total price after tax.

price=float(input("Please insert the product price ($): "))

tax\_rate=float(input("Please insert the product tax\_rate (%):"))

def calculate\_total (price,tax\_rate) :

&nbsp;     return price +(price\*tax\_rate/100)

final\_price=calculate\_total (price,tax\_rate)

print(f'The final price is {final\_price:.2f} ')





\#Task — Write a function that checks if a number is EVEN or ODD.



while True: 

&nbsp;   ask=(input("Do you want to check odd or even ?:")).lower()

&nbsp;   if ask =="yes" or ask =="y":

&nbsp;       user =int(input("Please insert a number to know odd/even :"))

&nbsp;       def know\_odd\_even(number):

&nbsp;           if number %2 ==0:

&nbsp;               return(f'{number} is an even number !')

&nbsp;           else:

&nbsp;               return(f"{number} is an odd number!")

&nbsp;       result=know\_odd\_even(user)

&nbsp;       print(result)

&nbsp;       continue

&nbsp;   else :

&nbsp;       print("Thank You !")

&nbsp;   break 

import random 

list= \[3, -1, 0, 7, -5, 0]

x=random.choice(list)

def know\_num(number) :

&nbsp;   if x >0:

&nbsp;      return (f"{number} is a positive number")

&nbsp;   elif x<0:

&nbsp;       return(f"{number} is a negetive number")

&nbsp;   else:

&nbsp;       return(f"{number} is Zero (0)")

result=know\_num(x)

print(result)





numbers = \[10, 3, 5, 20, 8]



def num(numbers):

&nbsp;   total = 0

&nbsp;   count = 0

&nbsp;   highest = numbers\[0]

&nbsp;   lowest = numbers\[0]

&nbsp;   

&nbsp;   for i in numbers:

&nbsp;       total += i

&nbsp;       count += 1



&nbsp;       if i > highest:

&nbsp;           highest = i



&nbsp;       if i < lowest:

&nbsp;           lowest = i



&nbsp;   average = total / count

&nbsp;   return total, count, highest, lowest, average



result = num(numbers)

print(result)



\#Write a function that checks a student’s grade based on their marks.

def check\_grade(marks) :

&nbsp;   if marks>= 80 :

&nbsp;       return (f"Marks is {marks} and Grade is A")

&nbsp;   elif marks >= 70 :

&nbsp;       return (f"Marks is {marks} and Grade is A-")

&nbsp;   elif marks >=65 :

&nbsp;       return (f"Marks is {marks} and Grade is B")

&nbsp;   elif marks >=60:

&nbsp;       return (f"Marks is {marks} and Grade is Pass")

&nbsp;   else :

&nbsp;        return (f"Marks is {marks} and Grade is Fail")

while True:

&nbsp;   user=input("Please insert your number to know the Grade : ") 

&nbsp;   if user.lower()=="stop":

&nbsp;       print("Thanks, Goodbye !")

&nbsp;       break

&nbsp;   if user.isnumeric():

&nbsp;       user=int(user)

&nbsp;       result=check\_grade(user)

&nbsp;       print(result)

&nbsp;   else:

&nbsp;       print("Please insert vallid numeric value only")

