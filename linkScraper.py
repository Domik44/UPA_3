# Author: Dominik Pop
# Date: 22.12.2023
# Description: This file containes function used for getting url links of products.

from headerFile import get_text, sleep, HEADER

# Global variables
prefix = 'https://airsoftshop.cz'


def get_links(url):
    """
    This function is used for getting links of products from given url.

    :param url: Link from which we are scraping links from.
    :return: Returns list of links
    """
    webText = get_text(url, HEADER)
    maxPage = int(webText.find(class_='last').getText()) + 1
    links = []
    for page in range(1, maxPage):
        webText = get_text(url+'?page='+str(page), HEADER)
        productsCont = webText.find(class_='products-container')
        products = productsCont.findAll(class_='product')
        for product in products:
            links.append(prefix + product.find('a').get('href'))
            print(prefix + product.find('a').get('href'))
        sleep(0.2)

    return links


def main():
    links = get_links('https://airsoftshop.cz/aeg-47-74')


if __name__ == '__main__':
    main()