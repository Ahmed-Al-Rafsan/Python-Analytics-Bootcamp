# Python for Data Analytics — Day 28



 **Combining Data with merge() \& join(**)





**#Task 1 :Create two DataFrames:products → ProductID, ProductName and sales → SaleID, ProductID, Quantity - Perform an inner merge.**

import pandas as pd 

products=pd.DataFrame({

&nbsp;   "ProductID":\[101,102,103,104],

&nbsp;         "ProductName":\["apple","pen","milk","soft drinks"],

})

sales=pd.DataFrame({"SaleID":\[4000,4001,4002,4003],

&nbsp;      "ProductID":\[101,102,103,105],

&nbsp;      "Quantity":\[100,50,450,300]

})

df=pd.merge(products,sales,on="ProductID",how="inner")

print(df\[\["ProductName","ProductID","SaleID","Quantity"]])







**#Task 2 :Using the same data, perform a left merge- Identify which products were never sold.**

import pandas as pd 

products=pd.DataFrame({

&nbsp;   "ProductID":\[101,102,103,104],

&nbsp;         "ProductName":\["apple","pen","milk","soft drinks"],

})

sales=pd.DataFrame({"SaleID":\[4000,4001,4002,4003],

&nbsp;      "ProductID":\[101,102,103,105],

&nbsp;      "Quantity":\[100,50,450,300]

})

df=pd.merge(products,sales,on="ProductID",how="left")

print(df)

unsold\_product=df\[df\["SaleID"].isna()]

print(unsold\_product)







**#Task 3 (Analyst Thinking) From the merged DataFrame:Calculate total quantity sold per product**

import pandas as pd 

products=pd.DataFrame({

&nbsp;   "ProductID":\[101,102,103,104],

&nbsp;         "ProductName":\["apple","pen","milk","soft drinks"],

})

sales=pd.DataFrame({"SaleID":\[4000,4001,4002,4003],

&nbsp;      "ProductID":\[101,102,103,105],

&nbsp;      "Quantity":\[100,50,450,300]

})

df=pd.merge(products,sales,on="ProductID",how="left")

result=df.groupby("ProductID")\["Quantity"].sum()

print(result)







**#Task 4 - Rename columns neatly after merge:ProductName → Product ,Quantity → Units\_Sold**

import pandas as pd 

products=pd.DataFrame({

&nbsp;   "ProductID":\[101,102,103,104],

&nbsp;         "ProductName":\["apple","pen","milk","soft drinks"],

})

sales=pd.DataFrame({"SaleID":\[4000,4001,4002,4003],

&nbsp;      "ProductID":\[101,102,103,105],

&nbsp;      "Quantity":\[100,50,450,300]

})

df=pd.merge(products,sales,on="ProductID",how="left")

updated=df.rename(

&nbsp;  columns={'ProductName':"Product","Quantity":"Units\_Sold"}

)

print(updated)

