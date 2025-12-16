import csv
def read_salaries():
    with open ("data.csv","r") as f :
        reader=csv.reader(f)
        next(reader)
        salaries=[]
        for i in reader:
            salaries.append((int(i[2])))
        return salaries
salaries=read_salaries()
def average_salary(salaries):
    return round(sum(salaries)/len(salaries))
def highest_salary(salaries):
    return max(salaries)
def minimum_salary(salaries):
    return min(salaries)
if __name__=="__main__":
    print(f'Salary:{salaries}')
    print(f"Average Salary: {average_salary(salaries)}")
    print(f"Maximum Salary : {highest_salary(salaries)}")
    print(f"Minimum Salary : {minimum_salary(salaries)}")
        
       
 
        