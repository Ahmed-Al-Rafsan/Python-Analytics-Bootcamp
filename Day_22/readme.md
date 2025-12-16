# Python for Data Analytics — Day 22

# Topic: Lambda Functions + map() + filter()





**#Task 1 — Lambda Create a lambda function that returns the cube of a number and test it with 3.**



my\_fun=lambda x :x\*\*3

print(my\_fun(3))







**# Task 2 — map() :From this list: Create a new list where each value is increased by 5 using map().**



numbers = \[10, 20, 30, 40]

my\_fun= list(map(lambda x:x+5,numbers))

print(my\_fun)







**# Task 3 — filter() :From this list: Create a list of adults (age ≥ 18) using filter().** 

ages = \[12, 18, 25, 14, 30, 16]

revising\_members=list(filter(lambda x:x>=18,ages))

print(revising\_members)









**# Task 4 — Combined (Analyst Level) :From this list: First filter prices ≥ 150** 

**# Then apply 10% discount to the remaining prices ,Use lambda + filter + map.**



prices = \[100, 250, 300, 150, 90]

updated\_price=list(filter(lambda x:x>=150,prices))

discounted\_list=list(map(lambda x:x-x\*0.1,updated\_price))

print(updated\_price)

print(discounted\_list)

