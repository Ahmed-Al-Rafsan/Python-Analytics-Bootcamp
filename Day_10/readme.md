# **Day-10 \& 11** 



\#Task 1

\#Create a dictionary called book with:

\#title,author,year,price

\#Then print each value one by one.

book={

&nbsp;   "title":"Python The Ultimate Solution",

&nbsp;   "author": "Rafsan",

&nbsp;   "year":"2025",

&nbsp;   "price":200

}

for key,values in book.items():

&nbsp;   print(key,":" ,values)

\# Task - Add a new key "rating" to the dictionary and update "price"

book={

&nbsp;   "title":"Python The Ultimate Solution",

&nbsp;   "author": "Rafsan",

&nbsp;   "year":"2025",

&nbsp;   "price":200

}

\#Add a new key "rating" to the dictionary and update "price"

book\["rating"]=5.2

book\["price"]=250

for key,values in book.items():

&nbsp;   print(f" The value of {key} is {values}")

&nbsp;   profile={

&nbsp;   "name":"Rafsan",

&nbsp;   "age":31,

&nbsp;   "profession":"AI Engineer"

}

print(f'My name is {profile\["name"]}\\n'

f"My age is :{profile\["age"]}\\n"

f"As a profession I wanna be an {profile\["profession"]}")



user=input("Please insert a sentence : ")

words=user.split(" ")

for w in words:

&nbsp;   print(w)

skills = \["Python", "SQL", "Excel", "Power BI"]

sentence=(",").join(skills)

print(f'My skills are - {sentence}')

student = {

&nbsp;   "name": "Rafsan",

&nbsp;   "age": 31,

&nbsp;   "country": "Australia"

}

x=student.values()

y=\[str(i) for i in x]

joining=(",").join(y)

print(joining)

\#only\_values=str

