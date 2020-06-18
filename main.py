if __name__=="__main__":
  product_name=input("Enter the name of the product: ")
  try:
    search(product_name)
  except:
    #purpose of this block is to check if there is any error while searching the product on browser
    pass
def search(product_name):
  print("Search for a product")