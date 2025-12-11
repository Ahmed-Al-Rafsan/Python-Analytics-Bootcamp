# Day 16



**Task 1: Write Data to a File Using "w" Mode**



x="I am learning python"

with open("learning.txt","w") as f :

&nbsp;   f.write(x)

with open("learning.txt","r") as d:

&nbsp;       print(d.read())



**Task 2: Read Data from a File Using "r" Mode**



with open("file\_1.txt","w") as f :

&nbsp;   f.write("This is Rafsan\\n")

&nbsp;   f.write("I am learning Python\\n")





**Task 3: Append Data Using "a" Mode**



with open("file\_1.txt","a") as f :

&nbsp;   f.write("I want to be a data analyst\\n")

&nbsp;   f.write("I want to be a data engineer as well")

with open("file\_1.txt","r") as f :

&nbsp;   q=f.read()

&nbsp;   print(q)





**Task 4: Verify File Contents After Appending**



import os 

if os.path.exists("file\_1.txt"):

&nbsp;   print('file exists')

else:

&nbsp;   print("file does not exist !")





**Task 5: Check if a File Exists (os.path.exists)**

import os

if os.path.exists("lesson\_1.txt"):

&nbsp;   print("exists")

else:

&nbsp;   print("does not exists")

