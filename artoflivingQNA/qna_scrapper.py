from bs4 import BeautifulSoup
import requests
import csv
import time
from selenium import webdriver


#CSV FILE WRITE
csv_file=open('scrapped_data.csv','w',encoding='utf-8')
csv_writer=csv.writer(csv_file)
csv_writer.writerow(['Questions','Answer'])

def render_page(url):
    #set chromedriver path from your local machine
    driver = webdriver.Chrome(executable_path="C:\\Users\\jerry\\chrome_driver\\chromedriver.exe")
    driver.get(url)
    time.sleep(3)
    r = driver.page_source
    driver.quit()
    return r

def qna(my_url):

    #FETCHING page
    s = render_page(my_url)

    soup=BeautifulSoup(s,"lxml")

    for content in soup.findAll('div',class_="question-answer-container contextual-links-region"):
        questions=content.find('div',class_="question").text
        answers=content.find('div',class_="answer").text
        csv_writer.writerow([questions,answers])

    try:
        next=soup.find('li',class_="pager-next").a['href']
        if(next!=None):
            qna("https://www.artofliving.org"+next)

    except Exception as e:
        print("Finished")




url=input("Enter the url you want to scrap")
qna(url)
csv_file.close()
