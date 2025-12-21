#Task 1-Create a DataFrame with:Date,Orders,Extract Year & Month
import pandas as pd
data=pd.DataFrame(
    {"Date":["10-02-2025","15-04-2025","27-07-2025","31-12-2025"],
     "Orders":[250,120,144,570]
    }
)
data["Date"]=pd.to_datetime(data["Date"],dayfirst=True)
data["Month"]=data["Date"].dt.month
data["Year"]=data["Date"].dt.year
print(data)

#Task 2 - Filter only records after a given date
import pandas as pd
data=pd.DataFrame(
    {"Date":["10-02-2025","15-04-2025","27-07-2025","31-12-2025"],
     "Orders":[250,120,144,570]
    }
)
data["Date"]=pd.to_datetime(data["Date"],dayfirst=True)
filter_date=data[data["Date"]>="2025-05-01"]
print(filter_date)

#Task 3 (Analyst Thinking)-Calculate total orders per month
import pandas as pd
data=pd.DataFrame(
    {"Date":["10-02-2025","15-04-2025","27-07-2025","31-12-2025"],
     "Orders":[250,120,144,570]
    }
)
data["Date"]=pd.to_datetime(data["Date"],dayfirst=True)
data["Month"]=data["Date"].dt.month
total_orders=data.groupby("Month")["Orders"].sum()
print(total_orders)

#Task 4 - Find which month has the highest total orders
import pandas as pd
data=pd.DataFrame(
    {"Date":["10-02-2025","15-04-2025","27-07-2025","31-12-2025"],
     "Orders":[250,120,144,570]
    }
)
data["Date"]=pd.to_datetime(data["Date"],dayfirst=True)
data["Month"]=data["Date"].dt.month
monthly_total=data.groupby("Month")["Orders"].sum()
highest_month=monthly_total.idxmax()
highest_orders=monthly_total.max()
print(f"The highest selling month is {highest_month} and highest_orserd amount is {highest_orders}")