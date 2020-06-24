"""
Flipkart module
"""
from urllib.parse import quote
import requests
from bs4 import BeautifulSoup
from tabulate import tabulate


def get_product_details(products, div_or_a, name_tag):
    """
    this function will help us to provide products details
    """
    product_details_array = []

    for product in products:
        product_details = dict()

        product_details["name"] = product.find(div_or_a, {"class": name_tag}).text

        product_details["price"] = product.find("div", {"class": "_1vC4OE"}).text

        product_rating = product.find("div", {"class": "hGSR34"})
        product_details["rating"] = (
            product_rating.text if product_rating else "flipkart Assured"
        )

        product_details_array.append(product_details)

    return product_details_array


def display_products(products):
    """
    Display the products details to user
    """

    header = products[0].keys()
    rows = [x.values() for x in products]
    print(tabulate(rows, header, tablefmt="grid"))


def get_products(url):
    """
    Sending request to url
    """
    req = requests.get(url)

    soup = BeautifulSoup(req.text, "lxml")
    # product      seach  name_tag    price_tag   rating_tag
    product_type1 = soup.findAll(
        "div", {"class": "_3liAhj"}
    )  # product_typ1   a    _2cLu-l   div _1vC4OE   div hGSR34
    product_type2 = soup.findAll(
        "div", {"class": "_1SSAGr"}
    )  # product_type2   a    _2mylT6   div _1vC4OE  div HGSR34
    product_type3 = soup.findAll(
        "div", {"class": "_3O0U0u"}
    )  # product_type3  div  _3wU53n   div _1vC4OE div hGSR34

    product_details = []
    if product_type1:
        product_details = get_product_details(
            product_type1, div_or_a="a", name_tag="_2cLu-l"
        )

    elif product_type2:
        product_details = get_product_details(
            product_type2, div_or_a="a", name_tag="_2mylT6"
        )

    elif product_type3:
        product_details = get_product_details(
            product_type3, div_or_a="div", name_tag="_3wU53n"
        )

    if not product_details:
        print("Sorry, We couldn't find your product!!!")

    display_products(product_details)


def main():
    """
    Main function
    """
    get_products(
        "https://www.flipkart.com/search?q=" + quote(input("Enter product name: "))
    )


if __name__ == "__main__":
    main()
