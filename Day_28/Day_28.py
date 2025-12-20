#Task 1 :Create two DataFrames:products → ProductID, ProductName and sales → SaleID, ProductID, Quantity - Perform an inner merge.
import pandas as pd 
products=pd.DataFrame({
    "ProductID":[101,102,103,104],
          "ProductName":["apple","pen","milk","soft drinks"],
})
sales=pd.DataFrame({"SaleID":[4000,4001,4002,4003],
       "ProductID":[101,102,103,105],
       "Quantity":[100,50,450,300]
})
df=pd.merge(products,sales,on="ProductID",how="inner")
print(df[["ProductName","ProductID","SaleID","Quantity"]])

#Task 2 :Using the same data, perform a left merge- Identify which products were never sold.
import pandas as pd 
products=pd.DataFrame({
    "ProductID":[101,102,103,104],
          "ProductName":["apple","pen","milk","soft drinks"],
})
sales=pd.DataFrame({"SaleID":[4000,4001,4002,4003],
       "ProductID":[101,102,103,105],
       "Quantity":[100,50,450,300]
})
df=pd.merge(products,sales,on="ProductID",how="left")
print(df)
unsold_product=df[df["SaleID"].isna()]
print(unsold_product)


#Task 3 (Analyst Thinking) From the merged DataFrame:Calculate total quantity sold per product
import pandas as pd 
products=pd.DataFrame({
    "ProductID":[101,102,103,104],
          "ProductName":["apple","pen","milk","soft drinks"],
})
sales=pd.DataFrame({"SaleID":[4000,4001,4002,4003],
       "ProductID":[101,102,103,105],
       "Quantity":[100,50,450,300]
})
df=pd.merge(products,sales,on="ProductID",how="left")
result=df.groupby("ProductID")["Quantity"].sum()
print(result)

#Task 4 - Rename columns neatly after merge:ProductName → Product ,Quantity → Units_Sold
import pandas as pd 
products=pd.DataFrame({
    "ProductID":[101,102,103,104],
          "ProductName":["apple","pen","milk","soft drinks"],
})
sales=pd.DataFrame({"SaleID":[4000,4001,4002,4003],
       "ProductID":[101,102,103,105],
       "Quantity":[100,50,450,300]
})
df=pd.merge(products,sales,on="ProductID",how="left")
updated=df.rename(
   columns={'ProductName':"Product","Quantity":"Units_Sold"}
)
print(updated)