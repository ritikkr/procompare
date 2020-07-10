"""Contains helpers functions to scrap products."""


def get_products(website_module, search_item, only_one=False):
    """Returns array of products using given search item."""
    url = website_module.make_url(search_item)

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0",
        "Accept-Encoding": "gzip, deflate",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "DNT": "1",
        "Connection": "close",
        "Upgrade-Insecure-Requests": "1",
    }

    product_soup = website_module.make_products_soup(url, headers)

    return website_module.product_array_from_product_soup(product_soup, only_one)