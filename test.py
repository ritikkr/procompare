"""Testing script for procompare app."""

import flipkart

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
    for item in search_terms:
        if flipkart.get_products(item):
            # product found
            continue
        else:
            print("flipkart test failed for search term " + item)
            exit()      
def test_amazon_get_product():
    for item in search_terms:
        if amazon.get.proudcts(item):
            #product found
            continue
        else:
            print("Amazon test failed for search term "+item)
            exit()

test_flipkart_get_product()
test_amazon_get_product()