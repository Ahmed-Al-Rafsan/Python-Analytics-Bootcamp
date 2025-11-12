# **Day-2**



\#Task 2:

\#Write a short program that:

\#Takes a user’s input for age (as string)

\#Converts it to integer

\#Prints “In 5 years you’ll be \_\_\_ years old.”



x= input("What is your age ? :\\n")

y=int(x)

print( f"In 5 years you'll be {5+y} years old")





\#Task 3:

\#Create a variable quote = "Data is the new oil" and:

\#Print the word "new" using slicing

\#Replace "oil" with "gold"

\#Convert the entire string to uppercase

x=list("Data is the new oil")

print(x)

y=str(x\[0]+x\[1]+x\[2]+x\[3]+x\[4]+x\[5]+x\[6]+x\[7]+x\[8]+x\[9]+x\[10]+x\[11]+x\[12]+x\[13]+x\[14]+x\[15]+x\[16]+x\[17]+x\[18])

print(y.replace("oil","gold").upper())



\#Task 4 — Practical Use Cases of Type Conversion \& String Handling

\#Write a Python script that performs the following:

\#Create three variables:

\#price\_str = "45.6"

\#quantity\_str = "3"

\#product = "Protein Bar"

\#Convert price\_str and quantity\_str to float and int types.

\#Calculate the total cost by multiplying price × quantity.

\#Then convert the total cost back into a string, join it with other words using 

\# " ".join() to form the same sentence again, and print it once more.

price\_str = "45.6"

quantity\_str = "3"

product = "Protein Bar"

x=float(price\_str)

quantity\_str = "3"

y=int(quantity\_str)

cost =x\*y 

print(f'The total cost is {cost}')

z=str(cost)

k="The total cost is"

kz=\[k+" "+z]

final=" ".join(kz)

print(final))





## **#Day 2 Mini Project — “Basic Info Program”**



\#Create a short interactive script that:

\#Takes user input (name, age, hobby)

\#Converts the age to an integer

\#Prints a clear, personalized message using f-strings

\#Calculates and displays how old the person will be in 10 years



user\_name=input("What is your Name :").lower()  

while True:

&nbsp;   try:

&nbsp;       user\_age=int(input("What is your age ? : "))

&nbsp;   except ValueError:

&nbsp;       print("Please Enter Numbers Only")

&nbsp;       continue

&nbsp;   user\_hobby=input("What is your favourite hobby ? :")

&nbsp;   print(f'After 10 years you will be {user\_age+10} years old ')

&nbsp;   break

&nbsp;   

