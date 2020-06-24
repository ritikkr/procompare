"""Function related to Flipkart website for scraping data."""

from urllib.parse import quote
import re
import requests
from bs4 import BeautifulSoup



def _get_product_details(products):
    product_details_array = []

    for product in products:
        product_details = dict()

        # layout    product   search  name_tag        price_tag   rating_tag
        # murga     _3liAhj   dreamer a _2cLu-l div   _1vC4OE     div hGSR34
        # suit      _1SSAGr   suit    a _2mylT6 div   _1vC4OE
        # mobile    _3O0U0u   mobile  div _3wU53n div _1vC4OE     div hGSR34

        product_details["name"] = product.find(
            re.compile("(a|div)"), {"class": re.compile("(_2cLu-l|_2mylT6|_3wU53n)")}
        ).text

        product_details["price"] = product.find("div", {"class": "_1vC4OE"}).text

        product_rating = product.find("div", {"class": "hGSR34"})
        product_details["rating"] = product_rating.text if product_rating else "0.0"

        product_details_array.append(product_details)

    return product_details_array


def get_products(search_item):
    """Returns the product array containing dictionary of products."""

    url = "https://www.flipkart.com/search?q=" + quote(search_item)

    soup = BeautifulSoup(requests.get(url).text, "lxml")

    products = soup.findAll("div", {"class": re.compile(("_3liAhj|_1SSAGr|_3O0U0u"))})

    products_details = _get_product_details(products)

    return products_details
