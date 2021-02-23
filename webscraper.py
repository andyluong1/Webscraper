from bs4 import BeautifulSoup 
import requests 
import csv

source = requests.get("https://www.newegg.com/Desktop-Graphics-Cards/SubCategory/ID-48?Tid=7709&PageSize=60").text

soup = BeautifulSoup(source, "html.parser")

csv_file = open("Graphics_card_scraper.csv", "w")

csv_writer = csv.writer(csv_file)
csv_writer.writerow(["brand", "description", "rating", "price", "shipping"])

for item in soup.find_all("div", class_= "item-cell"):
    try:
        brand = item.div.div.a.img["title"]
    except Exception as identifier:
        brand = None
    print(brand)

    description = item.find("a", class_= "item-title").text
    print(description)

    try:
       rating = item.find("a", class_= "item-rating")["title"] 
    except Exception as identifier:
        rating = None
    
    print(rating)

    price = item.find("li", class_= "price-current").text  
    print(price)

    shipping = item.find("li", class_= "price-ship").text
    print(shipping)

    print()

    csv_writer.writerow([brand, description, rating, price, shipping])

csv_file.close() 