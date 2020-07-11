"""Compare 'product' price in just a few clicks
   from more than 1 shopping sites."""

import argparse

import amazon
import flipkart
import scrap_helper as sch

def main():
    """Driver code for 'procompare' app"""

    parser = argparse.ArgumentParser(
        description="compare prices of product from different sites"
    )
    parser.add_argument("product", help="name of the product")

    args = parser.parse_args()

    for product in sch.get_products(flipkart, args.product):
        print(product)
    

if __name__ == "__main__":
    main()