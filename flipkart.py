"""Function related to Flipkart website for scraping data."""

import re
import requests
from bs4 import BeautifulSoup
from product import Product


def _product_from_product_tag(product_tag):
    # layout    product   search  name_tag        price_tag   rating_tag
    # murga     _3liAhj   dreamer a _2cLu-l div   _1vC4OE     div hGSR34
    # suit      _1SSAGr   suit    a _2mylT6 div   _1vC4OE
    # mobile    _3O0U0u   mobile  div _3wU53n div _1vC4OE     div hGSR34

    name_tag = product_tag.find(
        re.compile("(a|div)"), {"class": re.compile("(_2cLu-l|_2mylT6|_3wU53n)")}
    )
    price_tag = product_tag.find("div", {"class": "_1vC4OE"})
    rating_tag = product_tag.find("div", {"class": "hGSR34"})

    name = name_tag.text if name_tag else "unknown-product"
    price = price_tag.text if price_tag else "Out of Stock"
    rating = rating_tag.text if rating_tag else "Flipkart Assured"

    return Product(name, price, rating)


def product_array_from_product_soup(product_soup, only_one):
    products = []

    for product_tag in product_soup:
        product = _product_from_product_tag(product_tag)
        products.append(product)

        if only_one:
            break

    return products


def make_products_soup(url, headers):
    return BeautifulSoup(requests.get(url, headers=headers).text, "lxml").findAll(
        "div", {"class": re.compile(("_3liAhj|_1SSAGr|_3O0U0u"))}
    )


def make_url(search_item):
    return "https://www.flipkart.com/search?q=" + "+".join(search_item.split())
