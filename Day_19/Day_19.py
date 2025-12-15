#Task 1 — Custom Math Module
#Create math_tools.py with:
#add(a, b)
#subtract(a, b)
#average(numbers)
#Use it from main.py.
import math_tools
print(math_tools.add(10,5))
print(math_tools.subtract(100,500))
print(math_tools.average([100,25,144,236,788]))

#Task 2 — Statistics Module
#Create stats_tools.py with:
#highest(numbers)
#lowest(numbers)
#Import and test from main.py.
def highest(numbers):
    return max(numbers)
def lowest(numbers):
    return min(numbers)

#Task_3:
import statistics
from datetime import datetime
data=[100,200,300,400,500,455,755,788,6544]
x=statistics.mean(data)
y=statistics.sqrt(100)
now=datetime.now()
print(x)
print(y)
print(now)

#Task_4:
def add(a,b):
    return a+b 
def subtract(a,b):
    return a-b
def average(numbers):
    return sum(numbers)/len(numbers)
#this block will run directly
if __name__=="__main__":
    print(add(4,5))
    print(subtract(54,14))
    print(average([100,200,500]))