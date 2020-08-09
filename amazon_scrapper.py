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

def amazon_pro(my_url):


    #CSV FILE WRITE
    csv_file=open('scrapped_data.csv','w',encoding='utf-8')
    csv_writer=csv.writer(csv_file)
    csv_writer.writerow(['Title','Price','Image','Description'])

    #FETCHING page
    page=render_page(my_url)

    #SCRAPPING


    soup=BeautifulSoup(page,'html5lib')

    content=soup.find(id="imgTagWrapperId")

    title=soup.find(id="productTitle").text

    price=''

    try:
        price=soup.find(id="priceblock_ourprice").text

    except Exception as e:
        try:
            price=soup.find('span',class_="a-size-base a-color-price a-color-price").text

        except Exception as e:
            price="Product is Unavailable Right Now"

    img=''

    if content is not None:

        img=content.img['src']


    if content is None:
        try:
            img=soup.find(id="ebooks-img-canvas").img['src']


        except Exception as e:
            try:
                img=soup.find(id="img-canvas").img['src']
            except Exception as e:
                img="None"


    details=''
    try:
        for ul in soup.findAll('ul',class_="a-unordered-list a-vertical a-spacing-mini"):
            for li in ul.findAll('span'):
                details+=li.text
        if details=='':
            print(dmska)
    except Exception as e:
        try:

            for frame in soup.findAll('iframe',id='bookDesc_iframe'):
                details=BeautifulSoup(details,features='lxml')

            print(details)

        except Exception as e:
            details="None"

    #STORING

    csv_writer.writerow([title,price,img,details])
    csv_file.close()
