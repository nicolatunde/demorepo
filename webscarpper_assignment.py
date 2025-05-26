# Scrape book information (title, price, and availability) from a website and perform basic analysis such as average price, most expensive book, and count of books in stock.
# Use the demo site: http://books.toscrape.com
# Count total number of books
# Calculate the average price
# Find the most expensive book
# Count how many books are in stock 
import requests as req
from bs4 import BeautifulSoup
import pprint
import json
# store_content = req.get('http://books.toscrape.com')
# soup = BeautifulSoup(store_content.content,"html.parser")

# # print(dir(soup))
# all_books_html = soup.find_all('article')

# print('Number of articles: ', len(all_books_html))

# all_prices = []
# for book in all_books_html:
#     price = book.find('p', 'price_color').get_text()
#     price_only = float(price.replace('£', ''))
#     # print(book.find('p', 'price_color').get_text())
#     all_prices.append(price_only)
#     print(book.find("h3").get_text().replace("...", "").strip() + ".")

# pprint.pprint(soup)

# print (all_prices)
# print (sum(all_prices))
# print(min(all_prices))
# print(max(all_prices))
# avg = sum(all_prices)/len(all_prices)


# sum, max, min

url = "https://www.scrapethissite.com/pages/simple/"
site_content = req.get(url)
# print (site_content)
site_content_html = (BeautifulSoup(site_content.content, "html.parser"))
allcountry = site_content_html.find_all( "div","col-md-4 country")
country_count = 0
country_dict = []
if site_content.status_code == 200 :
    for country in allcountry:
        country_count += 1
        contry_each_disct = country.find("h3").get_text().strip()
        print('Country disct: ', contry_each_disct)
        # country_dict.append(contry_each_disct)
        # print(country)
       
        break


