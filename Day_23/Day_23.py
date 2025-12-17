#Task 1 — Conditional Transformation .From this list: Create a new list where: Numbers ≥ 10 are squared ,Numbers < 10 remain unchanged
numbers = [3, 7, 12, 5, 20, 8]
modified_list=[i**2 if i>=10 else i for i in numbers]
print(modified_list)

#Task 2 — Multiple Conditions : From this list:Create a list that contains: Only numbers divisible by both 5 and 10
numbers = [5, 10, 15, 20, 25, 30]
modified_list=[i for i in numbers if i%5==0 and i%10==0 ]
print(modified_list)

#Task 3 — String Filtering + Transformation ,From this list:Create a new list that:Keeps words with length > 3Converts them to UPPERCASE
words = ["data", "science", "ai", "python", "ml"]
modified_list=[i.upper() for i in words if len(i)>3]
print(modified_list)

#Task 4 — Analyst Mindset (Clean Data)From this list: Create a new list that:Removes invalid values (None) Keeps only scores ≥ 50
scores = [45, 78, None, 90, 55, None, 32]
modified_list=[i for i in scores if i is not None and i >= 50]
print(modified_list)

# Task 5 — Nested List Comprehension (Real-World Style) Create one flat list that contains: Only values ≥ 200 
sales = [[100, 200, 300], [50, 400], [700, 20]]
modified_list=[values for sublist in sales for values in sublist if values >=200 ]
print(modified_list)