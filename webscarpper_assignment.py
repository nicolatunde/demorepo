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

# Count how many countries are listed on the page.
# Print the country with the largest and smallest population.
# Calculate the average population of all countries.
# For each country, compute its population density (people per km²): density = population / area. List the top 3 countries with the highest density.
# Find all countries whose capital city starts with the letter "A". Return a list of those countries and their capitals.
# Find countries with an area greater than 1,000,000 km²
# Find countries with an area less than 500 km²
# Get the country that has 0 population.



def get_element_text(e_name, classes=''):
    if classes:
        return country.find(e_name, classes).get_text().strip()
    return country.find(e_name ).get_text().strip()


url = "https://www.scrapethissite.com/pages/simple/"
try:
    site_content = req.get(url)
except:
    print("this user is not connected to internet")
    exit()

# print (site_content)
site_content_html = (BeautifulSoup(site_content.content, "html.parser"))

allcountry = site_content_html.find_all( "div","col-md-4 country")
country_count = 0
country_list_dict = []
all_country_total_population = 0

if site_content.status_code == 200:
    for country in allcountry:
        country_count += 1
        country_name = get_element_text("h3")
        country_capital = get_element_text("span","country-capital")
        country_population = get_element_text("span","country-population")
        country_land_mass = get_element_text("span", "country-area")
        country_dict = {"country_name": country_name, "country_capital": country_capital, "country_population": country_population, "country_landmass": country_land_mass}
        country_list_dict.append(country_dict)
        all_country_total_population += (int(country_population))

print("The total number of the country is ",country_count)
print("The average popolation of all country is",all_country_total_population/country_count)

greatest_population = {"name" : country_list_dict[0]["country_name"], "population" :country_list_dict[0]['country_population']}

lowest_population = {"name" : country_list_dict[0]["country_name"], "population" :country_list_dict[0]['country_population']}
all_country_density_info = []
counter = 1
for eachcountry in country_list_dict:

    if int(eachcountry["country_population"]) > int(greatest_population["population"]):
        greatest_population = {"name" : eachcountry["country_name"], "population" :eachcountry['country_population']}
    

    if int(eachcountry["country_population"]) < int(lowest_population["population"]):
        lowest_population = {"name" : eachcountry["country_name"], "population" :eachcountry['country_population']}

    if eachcountry["country_population"] != "0":
        country_density_info = {"name":eachcountry["country_name"], "density" :(float(eachcountry['country_population']) / float(eachcountry["country_landmass"]))}
        all_country_density_info.append(country_density_info)

    else:
        country_density_info = {"name":eachcountry["country_name"], "density": 0 }
        all_country_density_info.append(country_density_info)
        # print(eachcountry)
    
    if eachcountry["country_name"][0] == "A":
        if counter == 1:
            print("These are the countries that start with letter A and their capital")
            counter += 1
        print("country",eachcountry["country_name"], "capital", eachcountry["country_capital"])
        
    if float(eachcountry["country_landmass"]) > 1000000:
        print("&&&&&&&%)))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))")
        print(eachcountry)



i = 1

all_country_density_info_sorted = sorted(all_country_density_info, key=lambda x: x['density'], reverse=True)
print("The top 3 countries with the highest density are")
for every_country in all_country_density_info_sorted[:3]:
    print(f"{i}.country name {every_country["name"]}  density {every_country["density"]}")
    i += 1


highest_population_density = {"name": all_country_density_info[0]["name"],  "density":all_country_density_info[0]["density"]} 
for one_country in all_country_density_info:
    # print(f"name of country: {one_country["name"]}, the country density is {round(one_country["density"],1)} people per km²")
    if one_country["density"] > highest_population_density["density"]:
        highest_population_density =  {"name": one_country["name"],  "density":one_country["density"]} 


print(f"{highest_population_density["name"]} has the highest population density of {highest_population_density["density"]}")

    
print(greatest_population["name"], "has the highest population", greatest_population["population"])


print(lowest_population["name"], "has the lowest population", lowest_population["population"])