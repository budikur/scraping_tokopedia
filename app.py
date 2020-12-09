import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
import os
import time

driver = webdriver.Chrome(executable_path=os.path.abspath('chromedriver'))
driver.get('https://www.tokopedia.com/search?q=laptop&source=universe&st=product')

SCROLL_PAUSE_TIME = 0.5
driver.execute_script("window.scrollBy(0,100)","")
time.sleep(SCROLL_PAUSE_TIME)
driver.execute_script("window.scrollBy(0,200)","")
time.sleep(SCROLL_PAUSE_TIME)
driver.execute_script("window.scrollBy(0,300)","")
time.sleep(SCROLL_PAUSE_TIME)
driver.execute_script("window.scrollBy(0,400)","")
time.sleep(SCROLL_PAUSE_TIME)
driver.execute_script("window.scrollBy(0,500)","")
time.sleep(SCROLL_PAUSE_TIME)
driver.execute_script("window.scrollBy(0,600)","")
time.sleep(SCROLL_PAUSE_TIME)
driver.execute_script("window.scrollBy(0,700)","")
time.sleep(SCROLL_PAUSE_TIME)
driver.execute_script("window.scrollBy(0,800)","")
time.sleep(SCROLL_PAUSE_TIME)
driver.execute_script("window.scrollBy(0,900)","")
time.sleep(SCROLL_PAUSE_TIME)
driver.execute_script("window.scrollBy(0,1000)","")
time.sleep(SCROLL_PAUSE_TIME)

# SCROLL_PAUSE_TIME = 3
# # Get scroll height
# last_height = driver.execute_script("return document.body.scrollHeight")
# while True:
#     # Scroll down to bottom
#     driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#
#     # Wait to load page
#     time.sleep(SCROLL_PAUSE_TIME)
#
#     # Calculate new scroll height and compare with last scroll height
#     new_height = driver.execute_script("return document.body.scrollHeight")
#     if new_height == last_height:
#         break
#     last_height = new_height
#     time.sleep(SCROLL_PAUSE_TIME)

products = []
prices = []
images = []

content = driver.page_source
# print(content)
# THIS IS FOR CHECK THE PAGE IS SUITABLE OR NOT
# f = open('./page1.html', 'w+')
# f.write(content)
# f.close()

# content = driver.page_source
soup = BeautifulSoup(content, features="html.parser")

# print(soup)
# soup = BeautifulSoup(open('./page1.html'), 'html.parser')
i=1
for link in soup.find_all('div',class_="css-1g20a2m"):
    product = link.find('div', class_="css-18c4yhp")
    print(i, product.get_text())
    products.append(product.get_text())
    # ===================================
    image = link.find('img', class_="success fade")
    print(image['src'])
    images.append(image)
    # ===================================
    price = link.find('div', class_="css-rhd610")
    print(price.get_text())
    prices.append(price.get_text())
    # ===================================
    i+=1
print(i)

df = pd.DataFrame({'Product Name':products,'Price':prices,'Images':images})
df.to_csv('tokopedia.csv',index=False,encoding='utf-8')
