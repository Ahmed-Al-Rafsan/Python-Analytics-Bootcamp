# **Day \_ 5 :**

\#Task 1 — Skip negative numbers

nums = \[5, -3, 10, -1, 7, 0, -9]

for i in nums :

&nbsp;   if i < 0:

&nbsp;       continue

&nbsp;   print(i)

\#Task 2 — Stop when “stop” appears

words = \["apple", "banana", "stop", "mango", "orange"]

for i in words : 

&nbsp;   if i == "stop":

&nbsp;       break 

&nbsp;   print(i)

\#Task 3 — Count how many even numbers before 0

values = \[2, 4, 6, 7, 8, 10, 0, 12, 14]

count=0

for i in values:

&nbsp;   if i ==0:

&nbsp;       break

&nbsp;   if i % 2 ==0:

&nbsp;       count+=1

print(count)

\#Task 4 — Print all characters except vowels

word = "Rafsan"

for i in word:

&nbsp;   if i in  ("a","e","i","o","u") :

&nbsp;       continue

&nbsp;   print(i)

\#Task 5 — Find the first number greater than 50

numbers=\[]

for i in list(range(60)):

&nbsp;   if i >50 :

&nbsp;       numbers.append (i)

print(numbers\[0])

\#Task 6 — Count vowels and consonants in a word

\#Write a program that:

\#Takes a word

\#Counts vowels

\#Counts consonants

\#Prints both numbers    





while True :

&nbsp;   vowel=0

&nbsp;   consonant=0

&nbsp;   user=(input("Please input a word :")).lower()

&nbsp;   if not user.isalpha():

&nbsp;           print("Please enter only a word !") 

&nbsp;           continue

&nbsp;   for i in user :

&nbsp;           if i in 'aeiou' :

&nbsp;               vowel+=1

&nbsp;           else:

&nbsp;               consonant +=1

&nbsp;   break 

print(vowel)

print(consonant)









