"""Function related to Flipkart website for scraping data."""

from urllib.parse import quote
import re
import requests
from bs4 import BeautifulSoup
from product import Product


def __get_product_details(products, only_one):
    product_details_array = []

    for product in products:
        # layout    product   search  name_tag        price_tag   rating_tag
        # murga     _3liAhj   dreamer a _2cLu-l div   _1vC4OE     div hGSR34
        # suit      _1SSAGr   suit    a _2mylT6 div   _1vC4OE
        # mobile    _3O0U0u   mobile  div _3wU53n div _1vC4OE     div hGSR34

        product_name_tag = product.find(
            re.compile("(a|div)"), {"class": re.compile("(_2cLu-l|_2mylT6|_3wU53n)")}
        )
        product_name = product_name_tag.text if product_name_tag else ""

        product_price_tag = product.find("div", {"class": "_1vC4OE"})
        product_price = product_price_tag.text if product_price_tag else ""

        product_rating_tag = product.find("div", {"class": "hGSR34"})
        product_rating = product_rating_tag.text if product_rating_tag else "0.0"

        product_details_array.append(
            Product(product_name, product_price, product_rating)
        )

        if only_one:
            break

    return product_details_array


def __make_products_soup(url):
    return BeautifulSoup(requests.get(url).text, "html.parser").findAll(
        "div", {"class": re.compile(("_3liAhj|_1SSAGr|_3O0U0u"))}
    )


def __make_url(search_item):
    return "https://www.flipkart.com/search?q=" + quote(search_item)


def get_products(search_item, only_one=False):
    """Returns an array containing Product class instance."""

    url = __make_url(search_item)
    soup = __make_products_soup(url)

    return __get_product_details(soup, only_one)
