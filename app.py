# import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
import os
import time

driver = webdriver.Chrome(executable_path=os.path.abspath('chromedriver'))
driver.get('https://www.tokopedia.com/search?q=laptop&source=universe&st=product')

SCROLL_PAUSE_TIME = 10
# Get scroll height
last_height = driver.execute_script("return document.body.scrollHeight")
while True:
    # Scroll down to bottom
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # Wait to load page
    time.sleep(SCROLL_PAUSE_TIME)

    # Calculate new scroll height and compare with last scroll height
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height

product = []
price = []
image = []

content = driver.page_source
soup = BeautifulSoup(content, features="html.parser")
# print(soup)
i=1
for link in soup.find_all('div',class_="css-1g20a2m"):
    if i>1:
        dataImg = link.find('img',class_="success fade")
        print(i-1,dataImg)
    i+=1
print(i)
