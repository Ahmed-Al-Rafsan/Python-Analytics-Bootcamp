#Temperature Converter
def tem_conv(temperature) : 
    return (temperature-32)*(5/9)
while True :
    user=(input("Please insert the temperature in Farenheit:")).lower()
    if user=="stop" or user=="s":
        print("Thank You !")
        break
    if user.replace(".","",1).replace("-","",1).isnumeric():
        user=float(user)
    else :
        print("please insert a vallid number ")
        continue
    result=tem_conv(user)
    print(result)
    
def calculator(num_1,num_2,op):

    if  op =="+":
        return num_1+num_2
    elif op =="-":
        return num_1-num_2
    elif op =="*":
        return num_1*num_2
    elif op =="/":
        return num_1/num_2
while True :
    ask=(input("Do you want to calculate ? ")).lower()
    if ask =="yes" or ask =="y":
        user_1= input("Please insert your first number: ")
        user_2= input("Please insert your 2nd number: ")
        operator=(input("+, -, *, / ? "))
        if not  (user_1.replace(".","",1).isnumeric() and user_2.replace(".","",1).isnumeric()):
            print("Please enter a vallid number")
            continue
        user_1=float(user_1)
        user_2=float(user_2)
        if operator not in ("+","-","*","/"):
            print("Please insert a vallid operator to calculate")
            continue
        if operator == "/" and user_2 ==0:
            print("Can't Devide by Zero")
            continue
        
        result=calculator(user_1,user_2,operator)
        print(result)    
       
    elif ask in ("no","n"):
        print("Thank You !")
        break

    
    