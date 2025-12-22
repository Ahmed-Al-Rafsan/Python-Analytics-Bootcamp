# Day-30 - Project Day ( Final Day of Python For Data Analytics)







The final project demonstrates an end-to-end data analysis workflow using Pandas, including:

\- Data creation and preparation

\- Data type handling and validation

\- Business-focused aggregations and groupby analysis

\- Derived metrics (Revenue per Unit)

\- Clear, human-readable analytical summaries



**Task 1️⃣ — Create the DataFrame**



**Task 2️⃣ — Fix data types**

Convert Date → datetime

Ensure Sales and Quantity are numeric





**Task 3️⃣ — Basic validation**

Check shape

Check column names

Check missing values



**Task 4️⃣ — Business questions**

Answer all using Pandas:

Total sales by Category

Total quantity sold by Product

Average sales per Region

Which month had the highest total sales?

Top 3 products by total sales





**Task 5️⃣ — Add insight columns**

Create:

Revenue\_per\_Unit = Sales / Quantity

Then:

Find the product with the highest revenue per unit





**Task 6️⃣ — Print a clean summary**

Print clear, human-readable insights, for example:

Best performing category

Best month for sales

Highest revenue product











import pandas as pd 

sales\_data={"Date":\["01-01-2025","05-01-2025","10-01-2025","15-01-2025","20-01-2025","25-01-2025","30-01-2025","04-02-2025","10-02-2025","15-02-2025"],

&nbsp;           "Product":\["Apple","Banana","Milk","Bread","Eggs","Rice","Chicken","Orange Juice","Coffee","Sugar"],

&nbsp;           "Category":\["Fruit","Fruit","Dairy","Bakery","Dairy","Grains","Meat","Beverage","Beverage","Grocery"],

&nbsp;           "Region":\["East","West","North","South","East","West","North","South","East","West"],

&nbsp;           "Sales":\[120, 80, 60, 45, 90, 150, 200, 110, 75, 50],

&nbsp;           "Quantity":\[5, 8, 3, 4, 6, 10, 7, 9, 2, 5]}

sales\_data\_frame=pd.DataFrame(sales\_data)

\#converting Dates to datetime

sales\_data\_frame\["Date"]=pd.to\_datetime(sales\_data\_frame\["Date"],dayfirst=True)

\#Basic validation,Check shape,Check column names,Check missing values

check\_shape=sales\_data\_frame.shape

check\_column\_names=sales\_data\_frame.columns

check\_missing\_values=sales\_data\_frame.isnull()

\#Adding insight columns -Creating:Revenue\_per\_Unit = Sales / Quantity 

sales\_data\_frame\["Revenue\_per\_Unit"]=(sales\_data\_frame\["Sales"]/sales\_data\_frame\["Quantity"])

\#Finding the product with the highest revenue per unit

highest\_revenue\_per\_unit=sales\_data\_frame\["Revenue\_per\_Unit"].max()

highest\_revenue\_generated\_product=sales\_data\_frame.loc\[sales\_data\_frame\["Revenue\_per\_Unit"].idxmax(),"Product"]

\#Total sales by Category

total\_sales\_cat=sales\_data\_frame.groupby("Category")\["Sales"].sum()

\#Total quantity sold by Product

total\_quantity=sales\_data\_frame.groupby("Product")\["Quantity"].sum()

\#Average sales per Region

average\_sales=sales\_data\_frame.groupby("Region")\["Sales"].mean()

\#Which month had the highest total sales?

sales\_data\_frame\["Date"]=pd.to\_datetime(sales\_data\_frame\["Date"],dayfirst=True)

highest\_selling\_month=sales\_data\_frame.groupby(sales\_data\_frame\["Date"].dt.month\_name())\["Sales"].sum().idxmax()

\#print(highest\_selling\_month)

\#Top 3 products by total sales

top\_3\_product=sales\_data\_frame.groupby("Product")\["Sales"].sum().sort\_values(ascending=False).head(3)

\#Visualizing final calculations:

print(f"Final Insights \\n")

print(f"Total Sales by Category : {total\_sales\_cat}")

print(f"Average Sales by Region : {average\_sales}")

print(f"Top 3 Products by Total Sales : {top\_3\_product}")

print(f"Month had the highest total sales : {highest\_selling\_month}")

print(f"Product has the highest Revenue per Unit:{highest\_revenue\_generated\_product}")

print(f"The highest revenue per unit product is Coffee, while Chicken generated the highest overall sales.")

