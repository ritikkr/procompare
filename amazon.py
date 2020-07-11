"""Function related to Amazon website for scraping data."""


import re
from bs4 import BeautifulSoup
import requests

from product import Product


def _trim_rating_text(rating_text):
    return re.compile("[0-9][.][0-9]").match(rating_text).group()


def _trim_link_text(link_text):
    return link_text[0 : link_text.rfind("/")]


def _product_from_product_tag(product_tag):
    name_tag = product_tag.find(
        "span", attrs={"class": "a-size-medium a-color-base a-text-normal"}
    )
    price_tag = product_tag.find("span", attrs={"class": "a-offscreen"})
    rating_tag = product_tag.find("span", attrs={"class": "a-icon-alt"})
    link_tag = product_tag.find("a", attrs={"class": "a-link-normal a-text-normal"})

    name = name_tag.text if name_tag else "unknown-product"
    price = price_tag.text if price_tag else "Out of Stock"
    rating = _trim_rating_text(rating_tag.text) if rating_tag else "Amazon Assured"
    link = "https://amazon.in"
    link += _trim_link_text(link_tag.get("href")) if link_tag else ""

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
    soup = BeautifulSoup(requests.get(url, headers=headers).text, "lxml")
    return soup.findAll(
        "div",
        attrs={
            "class": "sg-col-4-of-12 sg-col-8-of-16 sg-col-16-of-24 sg-col-12-of-20 sg-col-24-of-32 sg-col sg-col-28-of-36 sg-col-20-of-28"
        },
    )


def make_url(search_item):
    return "https://www.amazon.in/s?k=" + "+".join(search_item.split())
