# **Day-14 :**



\#TASK 1 — Default Parameters

def tea\_making(tea="x"):

&nbsp;   print(f"Here is your {tea}")

tea\_making(tea="Milk Tea with loaded sugar")



\#TASK 2 — Keyword Arguments

def profile(name ="Rafsan", country="Australia", skill="python"):

&nbsp;   return name,country,skill 

x,y,z=profile("Julia","Australia","python,SQL")

print(f"We have a new team member named {x}, Her country is {y} and her skill is {z}")





\#TASK 3 — Return Multiple Values

\#math\_ops(x, y)

\#Return:

\#sum

\#difference

\#product

def math\_ops(x,y):

&nbsp;   return x+y,x-y,x\*y

p=math\_ops(x=7,y=5)

print(p)





\#TASK 4 — Mini Project — Login Checker

\#Create a function:

\#login(username, password)

def login(user\_name="Rafsan",password=1234):

&nbsp;   if user\_name=="Rafsan" and password==1234:

&nbsp;       return "login successfull!"

&nbsp;   else:

&nbsp;       return "Invalid Credentials"

x=login(user\_name="Rafsana")

print(x)

y=login(user\_name="Rafsan",password=1234)

print(y)

