##Task 1 — Clean the Price List
products = ["$5.50", "$12.99", "$8.30", "$1.20"]
x=[]
for i in products :
   x.append(float(i.replace("$","")))
print(x)
#Task 2 — Count How Many Items Are Above 10 Dollars
products = ["$5.50", "$12.99", "$8.30", "$1.20","$13.20","$14.20"]
x=[]
for i in products :
   x.append(float(i.replace("$","")))
while True:
   Total=0
   for item in x:
      if item >= 10 :
         Total +=1
   break
print(Total)
#Task 3 — Format all floats to 2 decimal places
products = ["$5.50", "$12.99", "$8.30", "$1.20","$13.20","$14.20"]
x=[]
for items in products :
    x.append(float(items.replace("$","")))
for value in x:
   print(f"{value:.2f}")
#Task 4. Select only the values below 10
products = ["$5.50", "$12.99", "$8.30", "$1.20","$13.20","$14.20"]

x=list(((map(lambda p:float(p.replace("$","")),products))))
box=[]
for i in x : 
    if i<10:
        box.append(i)
print(box)

#Task 5 — Count Vowels & Consonants in a Word (Correct Version)
#This time, you must:
#Ask the user for a word
#Validate: only alphabets allowed
#Count:
#vowels
#consonants
#Print both numbers
#Loop again if the user enters invalid input
#Stop only when valid input is given
vowel=[]
vowel_count=0
consonent=[]
consonent_count=0
while True :
    user=(input("Please insert a Word :")).lower()
    if not user.isalpha():
        print("Only Alphabets are allowed , Please try a word!")
        continue
    for ch in user: 
      if ch in'aeiou':
        vowel.append(ch)
        vowel_count +=1
      else:
        consonent.append(ch) 
        consonent_count+=1
    break
print(f"Total Voewl {vowel_count} and Vowels are: {vowel}")
print(f"Total consonent {consonent_count} and consonent are: {consonent}")
   
   