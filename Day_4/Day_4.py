#Task 1 — Print square of each number
nums = [2, 5, 7, 10, 13]
for i in nums :
    print(i**2)
# Task 2 — Convert these to integers using a loop
heights = ["170cm", "165cm", "182cm", "159cm", "176cm"]
x=[]
for i in heights :
    x.append(int(i.replace("cm","")))
print(x)
#Task 3 — Calculate total price
Use a loop + float conversion to calculate the total sum.
products = ["$5.50", "$12.99", "$8.30", "$1.20"]
x=[]
for i in products :
    x.append(float(i.replace("$","")))
print(f"{sum(x):.3f}")
      

#Task 4 — Use range() to print
#all numbers from 1 to 50
#only even numbers from 2 to 20
#numbers from 10 to 1 (reverse)
x= list(range(1,51))
y=list(range(2,21,2))
z=list(range(10,0,-1))
print(x)
print(y)
print(z)

#Task 5 — Print index + value
cities = ["Sydney", "Melbourne", "Perth", "Adelaide"]
for i in range(len(cities)):
    print(i,cities[i])

