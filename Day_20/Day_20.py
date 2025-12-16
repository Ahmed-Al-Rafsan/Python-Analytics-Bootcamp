import csv
with open("data.csv","w",newline="") as f:
    writer=csv.writer(f)
    writer.writerow(["Name","Department","Salary"])
    writer.writerow(["Rafsan","Ai Engineer",54000])
    writer.writerow(["Xess","Data Engineer",45000])
    writer.writerow(["David","Data Scientist",51000])
    writer.writerow(["Willian","Data Analyst",48000])
