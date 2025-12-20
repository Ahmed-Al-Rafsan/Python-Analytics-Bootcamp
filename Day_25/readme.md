# \## Day 25 — Sorting Data (Analyst Mindset)



**Today’s focus was on sorting data structures the way data analysts do in real projects.**



**### Topics Covered:**

\- Sorting lists using `sorted()` (ascending \& descending)

\- Using `reverse=True`

\- Sorting strings by custom logic (`key=len`)

\- Sorting list of dictionaries using `lambda`

\- Ranking dictionary data using `.items()`

\- Understanding data structures before applying sort logic



**### Key Learnings:**

\- Always identify the structure of one element before sorting

\- Dictionaries use keys (`x\["price"]`)

\- Tuples use indexes (`x\[1]`)

\- Sorting logic directly prepares data for analysis, dashboards, and Pandas



This day focused more on \*\*thinking correctly about data\*\*, not just writing code.





**#Task 1 -Sort ascending,Sort descending**

numbers = \[45, 12, 89, 23, 67]

sorted\_list=sorted(numbers)

dec\_sorted\_list=sorted(numbers,reverse=True)

print(sorted\_list)

print(dec\_sorted\_list)





**#Task 2:Sort by length**

names = \["Data", "Analytics", "Python", "AI"]

sorted\_list=sorted(names,key=len)

print(sorted\_list)







**#Task 3 :Sort by price (low → high),Sort by price (high → low)**

products = \[

&nbsp;   {"product": "Laptop", "price": 1200},

&nbsp;   {"product": "Mouse", "price": 25},

&nbsp;   {"product": "Monitor", "price": 300}

]

price=sorted(products,key=lambda x:x\["price"])

high\_price=sorted(products,key=lambda x:x\["price"],reverse=True)

print(price)

print(high\_price)







**#Task 4 (Analyst Mindset):Sort students by marks,Highest scorer first**

students = {

&nbsp;   "Rafsan": 88,

&nbsp;   "Alex": 95,

&nbsp;   "Sam": 72

}

score\_list=sorted(students.items(),key=lambda x:x\[1],reverse=True)

print(score\_list)

