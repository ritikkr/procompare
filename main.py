"""Compare 'product' price in just a few clicks
   from more than 0(now) shopping sites."""


import argparse
import amazon


def main():
    """Driver code for 'procompare' app"""

    parser = argparse.ArgumentParser(description="Check Amazon's stock for product")
    parser.add_argument("product", help="name of the product")

    args = parser.parse_args()

    print(amazon.in_stock(args.product))


if __name__ == "__main__":
    main()
    print("i've added nothing in this")
