#Task 1️⃣ — Create the DataFrame
import pandas as pd 
sales_data={"Date":["01-01-2025","05-01-2025","10-01-2025","15-01-2025","20-01-2025","25-01-2025","30-01-2025","04-02-2025","10-02-2025","15-02-2025"],
            "Product":["Apple","Banana","Milk","Bread","Eggs","Rice","Chicken","Orange Juice","Coffee","Sugar"],
            "Category":["Fruit","Fruit","Dairy","Bakery","Dairy","Grains","Meat","Beverage","Beverage","Grocery"],
            "Region":["East","West","North","South","East","West","North","South","East","West"],
            "Sales":[120, 80, 60, 45, 90, 150, 200, 110, 75, 50],
            "Quantity":[5, 8, 3, 4, 6, 10, 7, 9, 2, 5]}
sales_data_frame=pd.DataFrame(sales_data)
#converting Dates to datetime
sales_data_frame["Date"]=pd.to_datetime(sales_data_frame["Date"],dayfirst=True)
#Basic validation,Check shape,Check column names,Check missing values
check_shape=sales_data_frame.shape
check_column_names=sales_data_frame.columns
check_missing_values=sales_data_frame.isnull()
#Adding insight columns -Creating:Revenue_per_Unit = Sales / Quantity 
sales_data_frame["Revenue_per_Unit"]=(sales_data_frame["Sales"]/sales_data_frame["Quantity"])
#Finding the product with the highest revenue per unit
highest_revenue_per_unit=sales_data_frame["Revenue_per_Unit"].max()
highest_revenue_generated_product=sales_data_frame.loc[sales_data_frame["Revenue_per_Unit"].idxmax(),"Product"]
#Total sales by Category
total_sales_cat=sales_data_frame.groupby("Category")["Sales"].sum()
#Total quantity sold by Product
total_quantity=sales_data_frame.groupby("Product")["Quantity"].sum()
#Average sales per Region
average_sales=sales_data_frame.groupby("Region")["Sales"].mean()
#Which month had the highest total sales?
sales_data_frame["Date"]=pd.to_datetime(sales_data_frame["Date"],dayfirst=True)
highest_selling_month=sales_data_frame.groupby(sales_data_frame["Date"].dt.month_name())["Sales"].sum().idxmax()
#print(highest_selling_month)
#Top 3 products by total sales
top_3_product=sales_data_frame.groupby("Product")["Sales"].sum().sort_values(ascending=False).head(3)
#Visualizing final calculations:
print(f"Final Insights \n")
print(f"Total Sales by Category : {total_sales_cat}")
print(f"Average Sales by Region : {average_sales}")
print(f"Top 3 Products by Total Sales : {top_3_product}")
print(f"Month had the highest total sales : {highest_selling_month}")
print(f"Product has the highest Revenue per Unit:{highest_revenue_generated_product}")
print(f"The highest revenue per unit product is Coffee, while Chicken generated the highest overall sales.")