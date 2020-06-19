import argparse
import Amazon

def main():
    parser = argparse.ArgumentParser(description="Check Amazon's stock for product")
    parser.add_argument("product", help="name of the product") 

    args = parser.parse_args()

    print(Amazon.in_stock(args.product))
    
if __name__ == '__main__':
    main()



