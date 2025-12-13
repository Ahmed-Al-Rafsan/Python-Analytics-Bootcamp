import csv 
with open(r"C:\Users\ahmed\OneDrive\Documents\Desktop\Airline_Delay_Cause.csv","r") as f :
    file=csv.reader(f)
    for i in range(20):
        print(next(file))


          