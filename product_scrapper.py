from amazon_scrapper import amazon_pro
from flipkart_scrapper import flipkart_pro

url=input("Enter the url you want to scrap")

if "amazon" in url:
    amazon_pro(url)

if "flipkart" in url:
    flipkart_pro(url)

print("Finished")
