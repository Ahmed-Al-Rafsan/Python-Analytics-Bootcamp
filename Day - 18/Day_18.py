#Task 1: Safe Average
numbers=[]
while True:
    try:
        user=int(input("Please insert numbers and press 0 to calculate: "))
        if user==0:
            break
        else:
            numbers.append(user)
    except:
        ValueError
        print("Please insert numbers only")
if len(numbers) >0:
    average=sum(numbers)/len(numbers)
    print(f"Average:{average}")


#Task 2: Dictionary Lookup (Safe & Clean)
marks={"science":85,
       "english":98,
       "math":77}
try:
    user=input("please insert the subject name: ")
    print(f"{user} :{marks[user]}")
except KeyError:
    print("inserted subject doesn't exist")
  

  #Task 3: File Reading Protection
try:
    import csv
    with open ("employees.csv","r") as f :
        reader=csv.reader(f)
        for i in reader:
            print(i)
except FileNotFoundError:
    print("file doesn't exist")

#Task 4: Combined Error Handling
try:
    user_1=int(input("Please insert the first number:"))
    user_2=int(input("Please insert the second number:"))
    number=user_1/user_2
    print(number)
except ValueError:
    print("please insert the number only")
except ZeroDivisionError:
    print("please use a correct divider apart from 0")
