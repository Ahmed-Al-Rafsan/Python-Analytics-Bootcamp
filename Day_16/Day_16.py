x="I am learning python"
with open("learning.txt","w") as f :
    f.write(x)
with open("learning.txt","r") as d:
        print(d.read())