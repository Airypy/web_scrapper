from bs4 import BeautifulSoup
import requests
import csv
import time
from selenium import webdriver

def render_page(url):
    #set chromedriver path from your local machine
    driver = webdriver.Chrome(executable_path="C:\\Users\\jerry\\chrome_driver\\chromedriver.exe")
    driver.get(url)
    time.sleep(3)
    r = driver.page_source
    driver.quit()
    return r


def flipkart_pro(my_url):

    #CSV FILE WRITE
    csv_file=open('scrapped_data.csv','w',encoding='utf-8')
    csv_writer=csv.writer(csv_file)
    csv_writer.writerow(['Title','Price','Image','Description'])

    #fetching web page
    page=render_page(my_url)

    #SCRAPPING

    soup=BeautifulSoup(page,"html5lib")

    title=soup.find('span',class_="_35KyD6").text

    price=soup.find('div',class_="_1vC4OE _3qQ9m1").text

    img=soup.find('div',class_="_3BTv9X _3iN4zu").img['src']


    details=''
    for li in soup.findAll('li',class_="_2-riNZ"):
        details+=li.text

    #STORING
    csv_writer.writerow([title,price,img,details])
    csv_file.close()
