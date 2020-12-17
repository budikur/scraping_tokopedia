import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
import os
import time
dict_product_list = []

def data_per_page(page,desired_product):
    driver = webdriver.Chrome(executable_path=os.path.abspath('chromedriver'))
    url = 'https://www.tokopedia.com/search?page=' + str(page) + '&q='+ str(desired_product) +'&source=universe&st=product'
    driver.get(url)
    scroll_down(driver)
    content = driver.page_source
    soup = BeautifulSoup(content, features="html.parser")

    i=1
    for link in soup.find_all('div',class_="css-1g20a2m"):
        products_links = link.find('a')['href']
        products_name = link.find('div', attrs={'class': 'css-18c4yhp'}).text
        # image = soup.find('img', attrs={'class': 'success fade'}).attrs['src']
        images = link.find('img', attrs={'class': 'success fade'}).attrs['src']
        prices = link.find('div', attrs={'class': 'css-rhd610'}).text

        dict_product = {
            'product_link': products_links,
            'product_name': products_name,
            'images': images,
            'price': prices
        }
        dict_product_list.append(dict_product)
        i+=1
    driver.close()
    print(dict_product_list)
    print(i)
    if dict_product_list == []:
        print('Oops, no products found on this page')
        print('exit')
        exit()

    df = pd.DataFrame(dict_product_list)
    df.to_csv('csv_file/page-'+ str(page) +'.csv', index=False, encoding='utf-8')
    dict_product_list.clear()
    page += 1
    data_per_page(page,desired_product)

def scroll_down(driver):
    SCROLL_PAUSE_TIME = 1
    down = 100
    for i in range(10):
        driver.execute_script("window.scrollBy(0," +str(down)+ ")", "")
        time.sleep(SCROLL_PAUSE_TIME)
        down += 100

def find_product():
    desired_product = input("What product you want to find?")
    return desired_product

if __name__ == '__main__':
    desired_product = find_product()
    # desired_product = 'baju bayi'
    page = 1
    data_per_page(page,desired_product)
