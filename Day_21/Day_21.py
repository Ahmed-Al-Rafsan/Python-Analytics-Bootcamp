#Task 1. Create a list of numbers from 1 to 10 and store their squares using list comprehension.
numbers=[]
for i in range(1,11):
    numbers.append(i)
print(numbers)
squares=[n*n for n in numbers]
print(squares)

# using list comprehension.
numbers=[i*i for i in range (1,11)]
print(numbers)