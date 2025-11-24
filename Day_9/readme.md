# **Day\_9 :**



\#Temperature Converter

def tem\_conv(temperature) : 

&nbsp;   return (temperature-32)\*(5/9)

while True :

&nbsp;   user=(input("Please insert the temperature in Farenheit:")).lower()

&nbsp;   if user=="stop" or user=="s":

&nbsp;       print("Thank You !")

&nbsp;       break

&nbsp;   if user.replace(".","",1).replace("-","",1).isnumeric():

&nbsp;       user=float(user)

&nbsp;   else :

&nbsp;       print("please insert a vallid number ")

&nbsp;       continue

&nbsp;   result=tem\_conv(user)

&nbsp;   print(result)

&nbsp;   

def calculator(num\_1,num\_2,op):



&nbsp;   if  op =="+":

&nbsp;       return num\_1+num\_2

&nbsp;   elif op =="-":

&nbsp;       return num\_1-num\_2

&nbsp;   elif op =="\*":

&nbsp;       return num\_1\*num\_2

&nbsp;   elif op =="/":

&nbsp;       return num\_1/num\_2

while True :

&nbsp;   ask=(input("Do you want to calculate ? ")).lower()

&nbsp;   if ask =="yes" or ask =="y":

&nbsp;       user\_1= input("Please insert your first number: ")

&nbsp;       user\_2= input("Please insert your 2nd number: ")

&nbsp;       operator=(input("+, -, \*, / ? "))

&nbsp;       if not  (user\_1.replace(".","",1).isnumeric() and user\_2.replace(".","",1).isnumeric()):

&nbsp;           print("Please enter a vallid number")

&nbsp;           continue

&nbsp;       user\_1=float(user\_1)

&nbsp;       user\_2=float(user\_2)

&nbsp;       if operator not in ("+","-","\*","/"):

&nbsp;           print("Please insert a vallid operator to calculate")

&nbsp;           continue

&nbsp;       if operator == "/" and user\_2 ==0:

&nbsp;           print("Can't Devide by Zero")

&nbsp;           continue

&nbsp;       

&nbsp;       result=calculator(user\_1,user\_2,operator)

&nbsp;       print(result)    

&nbsp;      

&nbsp;   elif ask in ("no","n"):

&nbsp;       print("Thank You !")

&nbsp;       break



&nbsp;   

&nbsp;   

