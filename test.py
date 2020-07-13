"""Testing script for procompare app."""

import sys
import flipkart
import amazon
import scrap_helper

search_terms = [
    "Kitchen utensils",
    "Sanitary products",
    "Miscellaneous goods",
    "Containers & wrapping",
    "Dyestuffs",
    "Public hygiene products",
    "Agents for control of infectious diseases",
    "Wood preservatives",
    "books",
    "DVDs",
    "music CDs",
    "videotapes",
    "software",
    "apparel",
    "baby products",
    "consumer electronics",
    "beauty products",
    "gourmet food",
    "groceries",
    "health and personal-care items",
    "industrial & scientific supplies",
    "kitchen items",
    "jewelry and watches",
    "lawn and garden items",
    "musical instruments",
    "sporting goods",
    "tools",
    "automotive items and toys & games",
]


def test_flipkart_get_product():
    """
    Testing products on flipkart module
    """
    print("Flipkart")
    for item in search_terms:
        if scrap_helper.get_products(flipkart, item):
            print("pass")
        else:
            print("flipkart test failed for search term " + item)


def test_amazon_get_product():
    """ 
    Testing products on amazon module
    """
    print("Amazon")
    for item in search_terms:
        if scrap_helper.get_products(amazon, item):
            print("pass")
        else:
            print("Amazon test failed for search term " + item)


test_flipkart_get_product()
test_amazon_get_product()
