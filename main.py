"""Compare 'product' price in just a few clicks
   from more than 0(now) shopping sites."""


import argparse
import flipkart


def main():
    """Driver code for 'procompare' app"""

    parser = argparse.ArgumentParser(
        description="compare prices of product from different sites"
    )
    parser.add_argument("product", help="name of the product")

    args = parser.parse_args()

    for product in flipkart.get_products(args.product):
        print(product)


if __name__ == "__main__":
    main()

      
