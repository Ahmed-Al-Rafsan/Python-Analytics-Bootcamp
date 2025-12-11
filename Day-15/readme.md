# **Day 15 of Python for Data Analytics :** 


Task 1 — Function Scope Demonstration (Local vs Global Variables)
---

x=50

def num():

&nbsp;   x=60

&nbsp;   return x

print(num())

print(x)



Task 2 — Safe List Modification Inside a Function
---



list=\[10,20,30,40,50,60]

def new\_list(a):

&nbsp;   a=a+\[999]

&nbsp;   return a

x=new\_list(list)

print(x)



### 

### Task 3 — Safe Dictionary Modification Using copy()

original ={"name":"Rafsan","age":31}

def profile(a):

&nbsp;   a=a.copy()

&nbsp;   a\["country"]="Australia"

&nbsp;   a\["sex"]="Male"

&nbsp;   return a

print(original)

print(profile(original))

print(original)



Task 4 — Average Calculator Function

---

x=\[10,20,30]

def avg\_num(a):

&nbsp;   total=sum(a)

&nbsp;   y=total/len(a)

&nbsp;   return y

print(x)

print((avg\_num(x)))



Task 5 — Filter Numbers Greater Than a Limit
---

number=\[10,15,18,22]

result=\[]

def num\_fun(a,limit):

&nbsp;   for i in a:

&nbsp;       if i>limit:

&nbsp;           result.append(i)

&nbsp;   return result

print(f"original:{number}")

print(f"function :{num\_fun(number,12)}")





Task 6 — Mini Project: Student Result Analyzer

---

marks={"Science":88,"Biology":97,"English":100}

def analyse(a):

&nbsp;   total=sum(a.values())

&nbsp;   average=total/len(a)

&nbsp;   highest=max(a,key=a.get)

&nbsp;   lowest=min(a,key=a.get)

&nbsp;   return total,average,highest,lowest

u=analyse(marks)

print(f'Total:{u\[0]}')

print(f"average :{u\[1]}")

print(f"Highest: {u\[2]}")

print(f"lowest: {u\[3]}")

