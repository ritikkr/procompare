"""Compare 'product' price in just a few clicks
   from more than 1 shopping sites."""

import argparse
from tabulate import tabulate
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
    print("Flipkart Result")
    serial_no = 1
    flipkart_result = sch.get_products(flipkart, args.product)
    for product in flipkart_result:
        print("[",serial_no,"] ",product)
        serial_no +=1
    print("\n-----------------------------------------------")
    print("Select a Product (1-",serial_no-1,") : ",end=" ")
    choice = int(input())
    print("------------------------------------------------")
    amazon_result = sch.get_products(amazon, flipkart_result[choice-1].name)
    amazon_product = [amazon_result[0].name,amazon_result[0].price,amazon_result[0].rating]
    flipkart_product = [flipkart_result[choice-1].name,flipkart_result[choice-1].price,flipkart_result[choice-1].rating]
    comparison_result = [amazon_product,flipkart_product]
    rowIDs =["Amazon :","Flipkart :"]
    print("\n\n\t\t COMPARISON RESULT ")
    print(tabulate(comparison_result, headers=["Item","Price","Rating"],showindex=rowIDs,tablefmt="grid"))
    
if __name__ == "__main__":
    main()
