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