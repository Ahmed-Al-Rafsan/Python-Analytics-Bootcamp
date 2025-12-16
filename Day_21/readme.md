# Python for Data Analytics — Day 21

# Topic: List Comprehension (Foundation of Data Analytics Thinking)



**#Task 1. Create a list of numbers from 1 to 10 and store their squares using list comprehension.**



numbers=\[]

for i in range(1,11):

&nbsp;   numbers.append(i)

print(numbers)

squares=\[n\*n for n in numbers]

print(squares)



**# using list comprehension.**

numbers=\[i\*i for i in range (1,11)]

print(numbers)













**# Task 2 From this list: Create a new list that contains only numbers greater than 10.**



numbers = \[5, 12, 18, 7, 25, 3]

my\_list=\[n for n in numbers if n>10]

print(my\_list)









**#Task 3 From this list: Create a new list where each word is capitalized.**



names = \["rafsan", "data", "analytics", "python"]

capitalized\_list=\[n.capitalize() for n in names ]

print(capitalized\_list)









**# Task 4 (Data Analyst Mindset) : Create a list of only passing marks (≥ 50).**





marks = \[45, 67, 89, 32, 90, 55]

passing\_students=\[n for n in marks if n>=50]

print(passing\_students)

