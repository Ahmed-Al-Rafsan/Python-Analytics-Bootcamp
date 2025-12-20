#Task 1 — Create DataFrame
import pandas as pd
data={"Name":["Rafsan","Emily","Cris","Tony"],
      "Age":[32,22,25,30],
      "Country":["Bangladesh","France","Australia","UAE"]
}
df=pd.DataFrame(data)
print(df)

#Task 2 — CSV Loading -Load a CSV file using Pandas and print: First 5 rows,Shape,Column names
import pandas as pd 
df=pd.read_csv(r"C:\Users\ahmed\Downloads\retail_sales_dataset.csv")
print(df.head(5))
print(df.shape)
print(df.columns)

#Task 3 — Exploration- Using the same DataFrame:Use info(),Identify:Total rows,Total columns,Data types
import pandas as pd 
df=pd.read_csv(r"C:\Users\ahmed\Downloads\retail_sales_dataset.csv")
#print(df)
print(df.info())
print(df.columns)
print(f"Total columns:{df.shape[1]}")
print(f"Total rows:{df.shape[0]}")
