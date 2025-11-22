#Task — Create a function that calculates the total price after tax.
price=float(input("Please insert the product price ($): "))
tax_rate=float(input("Please insert the product tax_rate (%):"))
def calculate_total (price,tax_rate) :
      return price +(price*tax_rate/100)
final_price=calculate_total (price,tax_rate)
print(f'The final price is {final_price:.2f} ')

#Task — Write a function that checks if a number is EVEN or ODD.

while True: 
    ask=(input("Do you want to check odd or even ?:")).lower()
    if ask =="yes" or ask =="y":
        user =int(input("Please insert a number to know odd/even :"))
        def know_odd_even(number):
            if number %2 ==0:
                return(f'{number} is an even number !')
            else:
                return(f"{number} is an odd number!")
        result=know_odd_even(user)
        print(result)
        continue
    else :
        print("Thank You !")
    break 
import random 
list= [3, -1, 0, 7, -5, 0]
x=random.choice(list)
def know_num(number) :
    if x >0:
       return (f"{number} is a positive number")
    elif x<0:
        return(f"{number} is a negetive number")
    else:
        return(f"{number} is Zero (0)")
result=know_num(x)
print(result)
#Write a function that checks a student’s grade based on their marks.
def check_grade(marks) :
    if marks>= 80 :
        return (f"Marks is {marks} and Grade is A")
    elif marks >= 70 :
        return (f"Marks is {marks} and Grade is A-")
    elif marks >=65 :
        return (f"Marks is {marks} and Grade is B")
    elif marks >=60:
        return (f"Marks is {marks} and Grade is Pass")
    else :
         return (f"Marks is {marks} and Grade is Fail")
while True:
    user=input("Please insert your number to know the Grade : ") 
    if user.lower()=="stop":
        print("Thanks, Goodbye !")
        break
    if user.isnumeric():
        user=int(user)
        result=check_grade(user)
        print(result)
    else:
        print("Please insert vallid numeric value only")