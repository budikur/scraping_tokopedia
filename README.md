# scraping_tokopedia.com

The tokopedia.com website has security so it cannot be scraped using requests.

In this program I use selenium to replace the role of "requests" so that I can extract data from tokopedia.com.

The csv files that I produce are of 2 types, they are:
1. "all_products.csv" which is to hold all data from all pages that are searched
2. some "page-x.csv" files that store data on each search page

If you want to retrieve data for each product I have prepared the function "def data_per_product (dict_product_list)" in the file "product_detail.py".

I made this source code as an exercise to make it more professional when working on scraping projects