#Print your name, country, and goal in one sentence.
print( "Name: Ahmed Al Rafsan, Country : Bangladesh, Goal: Is to be a Data Analyst")

#Store your height (in cm) and weight (in kg) → calculate and print your BMI (use weight / (height/100)**2).
height = "165.1 cm "
hgt=float(height.replace("cm","").strip())
weight="76 kg"
wt=float(weight.replace("kg","").strip())
BMI=wt/(hgt/100)**2
print(f'BMI={BMI:.2f}')
#Create a variable skills = ["SQL", "Python"] → print the list.
skill_1=["SQL"]
skill_2 =["Python"]
print(skill_1 +skill_2)

#Create a dictionary profile with your name, goal, and city → print it.
profile_dict={"name":"Ahmed AL Rafsan", "Goal":"Data Analyst","City":"Melbourne"}
print(profile_dict)