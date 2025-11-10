# Day\_1



\#Task 1. Print your name, country, and goal in one sentence.

print( "Name: Ahmed Al Rafsan, Country : Bangladesh, Goal: Is to be a Data Analyst")



\#Task 2 . Store your height (in cm) and weight (in kg) → calculate and print your BMI (use weight / (height/100)\*\*2).

height = "165.1 cm "

hgt=float(height.replace("cm","").strip())

weight="76 kg"

wt=float(weight.replace("kg","").strip())

BMI=wt/(hgt/100)\*\*2

print(f'BMI={BMI:.2f}')



\#Task 3.Create a variable skills = \["SQL", "Python"] → print the list.

skill\_1=\["SQL"]

skill\_2 =\["Python"]

print(skill\_1 +skill\_2)



\#Task 4. Create a dictionary profile with your name, goal, and city → print it.

profile\_dict={"name":"Ahmed AL Rafsan", "Goal":"Data Analyst","City":"Melbourne"}

print(profile\_dict)

