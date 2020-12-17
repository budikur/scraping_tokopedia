from selenium import webdriver
import os
from bs4 import BeautifulSoup

# def data_per_product(products_links):
def data_per_product(dict_product_list):
    dict_data_list = []
    i = 1
    for link in dict_product_list:
        driver = webdriver.Chrome(executable_path=os.path.abspath('chromedriver'))
        driver.get(link['product_link'])

        content = driver.page_source
        soup = BeautifulSoup(content, features="html.parser")

        title = soup.find('h1', attrs={'class': 'css-x7lc0h'}).text.strip()
        price = soup.find('h3', attrs={'class': 'css-c820vl'}).text.strip()
        terjual = soup.find('span', attrs={'data-testid': 'lblPDPDetailProductSuccessRate'}).text.strip().replace('Terjual ','')
        image = soup.find('img', attrs={'class': 'success fade'}).attrs['src']
        # description = soup.find('p', attrs={'data-testid': 'lblPDPDeskripsiProduk'})

        dict_data = {
            'title': title,
            'price': price,
            'terjual': terjual,
            'image': image
            # 'description': description
        }
        dict_data_list.append(dict_data)
        driver.close()
        print(link)
        break
        i += 1
    print(dict_data_list)
    print(i)

