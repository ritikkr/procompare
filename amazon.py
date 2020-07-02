"""Function related to Flipkart website for scraping data."""
from bs4 import BeautifulSoup
from tabulate import tabulate
import requests
from urllib.parse import quote

def __get_product_details(product_soup,only_one):
    product_details_array = []
    prev_name = ""
    for product in product_soup:
     
        product_details = dict()
        
        product_name_tag = product.find('span', {'class': 'a-size-medium a-color-base a-text-normal'}) 
        name = product_details['name'] = product_name_tag.text if product_name_tag else ""
       
        
        product_price_tag = product.find("span", {"class": "a-price-whole"})
        product_details['price'] = product_price_tag.text if product_price_tag else ""
        
        
        product_rating_tag = product.find("span", {"class": "a-icon-alt"})
        product_details['rating'] = product_rating_tag.text if product_rating_tag else "Assured"

        if(product_name_tag is None or  prev_name == name ):
            continue
        product_details_array.append(product_details)
        prev_name = name

        if only_one:
            break
        
    return (product_details_array)
    
def __make_products_soup(url):
    req = requests.get(url)
    soup = BeautifulSoup(req.text, "lxml")
    #soup = BeautifulSoup(amazon.html, "html.parser")
    
    product_soup = soup.select('div.s-main-slot,div.s-result-list,div.s-search-results,div.sg-row')
    return product_soup
    
def __make_url(search_item):
    
    url= "https://www.amazon.in/s?k="+((search_item.split(" ")).join("+"))
    return url
    
def get_products(search_item, only_one=False):
    """Returns an array containing Product class instance."""
    
    url = __make_url(search_item)
    soup = __make_products_soup(url)

    return __get_product_details(soup,only_one)
