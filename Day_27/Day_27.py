#Task 1 — Total Sales by Category
import pandas as pd

data = {
    "Category": ["Electronics", "Electronics", "Clothing", "Clothing", "Furniture"],
    "Region": ["East", "West", "East", "West", "East"],
    "Sales": [1200, 900, 500, 700, 400]
}

df = pd.DataFrame(data)
result=df.groupby("Category")["Sales"].sum()
print(result)

