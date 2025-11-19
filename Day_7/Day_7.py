#Print the total sum of only even numbers.
values = [12, 5, 7, 18, 22, 9, 10]
x=[]
for i in values :
    if i%2==0:
        x.append(i)
# printing the sum of only total numbers 
total=sum(x)
print(total)
#Task 2 :
#Filter only the prices greater than 50
#Increase each selected price by 10%
#Store them in a new list
#Print the final list with each value formatted to 2 decimals
prices = [15.50, 99.99, 45.00, 120.30, 9.99, 230.50]
x=[]
for i in prices : 
    if i > 50 :
        x.append(float(i*0.1))
final=[]
for k in x :
    final.append(f"{k:.2f}") 
print(final)

#Task : Ask the user for a word
#👉 Reverse it using a loop (no slicing, no shortcuts!)
#👉 Print the reversed result

while True :
    user=(input("Please write a word: ")).lower()
    x=" "
    if not user.isalpha()==True:
        print("Please insert a word only !")
        continue 
    else: 
        for i in user :
            x=i+x
        break
print(x)


#👉 Ask the user for a sentence
#👉 Count how many uppercase letters
#👉 Count how many lowercase letters
#👉 Print both numbers
#👉 Ignore spaces and punctuation (Python automatically handles this)
upper=0
upper_letter =""

lower=0
lower_letter=''

while True:
    user=input("Please write a sentence : ")
    valid =True 
    for i in user:
        if not i.isalpha() and i != " ":
            valid = False 
            break
    if not valid : 
        print("Please Write A Sentence Only! ")
        continue
    for i in user :
        if i.isupper():
                upper_letter+=i
                upper+=1
        elif i.islower():
            lower_letter+=i
            lower+=1
    break 
print(f"The Upper Letters are {upper_letter} which is Toatal {upper}")
print(f"The Lower Letters are {lower_letter} which is Toatal {lower}")