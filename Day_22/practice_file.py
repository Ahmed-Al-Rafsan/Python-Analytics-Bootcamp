# Task 4 — Combined (Analyst Level) :From this list: First filter prices ≥ 150 
# Then apply 10% discount to the remaining prices ,Use lambda + filter + map.
prices = [100, 250, 300, 150, 90]
updated_price=list(filter(lambda x:x>=150,prices))
discounted_list=list(map(lambda x:x-x*0.1,updated_price))
print(updated_price)
print(discounted_list)
