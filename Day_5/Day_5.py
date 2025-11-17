#Task 1 — Skip negative numbers
nums = [5, -3, 10, -1, 7, 0, -9]
for i in nums :
    if i < 0:
        continue
    print(i)
#Task 2 — Stop when “stop” appears
words = ["apple", "banana", "stop", "mango", "orange"]
for i in words : 
    if i == "stop":
        break 
    print(i)
#Task 3 — Count how many even numbers before 0
values = [2, 4, 6, 7, 8, 10, 0, 12, 14]
count=0
for i in values:
    if i ==0:
        break
    if i % 2 ==0:
        count+=1
print(count)
#Task 4 — Print all characters except vowels
word = "Rafsan"
for i in word:
    if i in  ("a","e","i","o","u") :
        continue
    print(i)
#Task 5 — Find the first number greater than 50
numbers=[]
for i in list(range(60)):
    if i >50 :
        numbers.append (i)
print(numbers[0])
#Task 6 — Count vowels and consonants in a word
#Write a program that:
#Takes a word
#Counts vowels
#Counts consonants
#Prints both numbers    


while True :
    vowel=0
    consonant=0
    user=(input("Please input a word :")).lower()
    if not user.isalpha():
            print("Please enter only a word !") 
            continue
    for i in user :
            if i in 'aeiou' :
                vowel+=1
            else:
                consonant +=1
    break 
print(vowel)
print(consonant)



