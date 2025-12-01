#Task 1
#Create a dictionary called book with:
#title,author,year,price
#Then print each value one by one.
book={
    "title":"Python The Ultimate Solution",
    "author": "Rafsan",
    "year":"2025",
    "price":200
}
for key,values in book.items():
    print(key,":" ,values)