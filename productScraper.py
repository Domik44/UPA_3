# Author: Dominik Pop
# Date: 22.12.2023
# Description: This file containes functions used for processing individual products from their URL.

from headerFile import get_text, sleep, Product
import sys


def process_input_args():
    """
    Function for processing input arguments of the script.
    :return: Returns lines of URLs as input, how many urls are to be processed as URLS and boolean if limit was set as limit.
    """
    input = None
    URLS = None
    limit = False
    if len(sys.argv) < 2:
        print("ERR wrong args!")
        exit(-1)
    else:
        if sys.argv[1] == 'STDIN':
            input = sys.stdin
        elif sys.argv[1] == 'FILE':
            input = open('urls.txt', 'r')
        else:
            print("ERR wrong args!")
            exit(-1)

        if len(sys.argv) > 2:
            URLS = int(sys.argv[2])
            limit = True

    return input, URLS, limit


def process_row(row):
    """
    Function for processing given row from parameters table.
    :param row: Row from table.
    :return: Returns name of attribute as key and its value as val.
    """
    columns = row.findAll("td")
    key = columns[0].getText().strip(': ').replace(' ', '_')
    val = columns[1].getText().strip()

    return key, val


def scrape_product(url):
    """
    Funcntion for scraping info about product from given URL.
    Function writes info about product to STDOUT.
    :param url: URL of the product.
    """
    webText = get_text(url + '/parametry')
    productName = webText.find("h1").getText()
    productPrice = webText.find(class_='price').getText().strip().replace('\xa0', ' ')
    product = Product(url, productName, productPrice)

    table = webText.find(class_='parameters')
    rows = table.findAll("tr")
    for row in rows:
        key, val = process_row(row)
        product.process_attribute(key, val)

    sys.stdout.buffer.write(product.encode())


def main():
    input, URLS, limit = process_input_args()
    counter = 0
    for link in input:
        if limit and counter == URLS:
            break
        scrape_product(link.strip('\n'))
        counter += 1
        if counter == 25:
            sleep(5)
            counter = 0

    if sys.argv[1] == 'FILE':
        input.close()

if __name__ == '__main__':
    main()