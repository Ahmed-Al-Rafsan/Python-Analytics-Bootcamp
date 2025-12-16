# Task 4 (Data Analyst Mindset) : Create a list of only passing marks (≥ 50).
marks = [45, 67, 89, 32, 90, 55]
passing_students=[n for n in marks if n>=50]
print(passing_students)