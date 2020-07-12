"""Compare 'product' price in just a few clicks
   from more than 1 shopping sites."""

import argparse
from tabulate import tabulate
import amazon
import flipkart
import scrap_helper as sch
import sys

def main():
    """Driver code for 'procompare' app"""

    print("-----------------------------------compare prices of product from different sites------------------------------------------")
    product_name = input("Enter Product Name: ")
    serial_no = 1
    flipkart_result = sch.get_products(flipkart, product_name)
    print("Flipkart Result")
    for product in flipkart_result:
        print("[",serial_no,"] ",product)
        serial_no +=1
    print("\n-----------------------------------------------")
    print("Select a Product (1-",serial_no-1,") : ",end=" ")
    choice = int(input())
    print("------------------------------------------------")
    amazon_result = sch.get_products(amazon, flipkart_result[choice-1].name)
    if (amazon_result == 0):
        print("!!!No particular product found on Amazon")
        sys.exit(0)
    amazon_product = [amazon_result[0].name,amazon_result[0].price,amazon_result[0].rating]
    flipkart_product = [flipkart_result[choice-1].name,flipkart_result[choice-1].price,flipkart_result[choice-1].rating]
    comparison_result = [amazon_product,flipkart_product]
    rowIDs =["Amazon :","Flipkart :"]
    print("\n\n\t\t COMPARISON RESULT ")
    print(tabulate(comparison_result, headers=["Item","Price","Rating"],showindex=rowIDs,tablefmt="grid"))
    
if __name__ == "__main__":
    main()
