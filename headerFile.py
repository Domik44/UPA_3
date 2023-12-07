from bs4 import BeautifulSoup
from requests import get
import random
from time import sleep

user_agents_list = [
    'Mozilla/5.0 (iPad; CPU OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.83 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36'
]
HEADER = {'User-Agent': random.choice(user_agents_list), 'Connection': 'keep-alive'}


def get_text(url, headers=None):
    """
    Function used for making request on given URL and parsing HTML structure.
    :param url: URL that we want to crape.
    :param headers: Headers to use with the request, not used if none are given.
    :return: Returns parsed HTML structure.
    """
    if headers is None:
        response = get(url)
    else:
        response = get(url, headers=headers)
    webText = BeautifulSoup(response.text, "html.parser")

    return webText


class Product:
    """
    Class used for storing info about scraped product.
    """
    def __init__(self, url, name, price):
        """
        Init method. URL, name and price are assigned, other attributes will be assigned later.
        :param url: URL of the product.
        :param name: Name of the product.
        :param price: Price of the product.
        """
        self.url = url
        self.name = '"' + name + '"'
        self.price = price
        self.speed = '-'
        self.mechabox = '-'
        self.body = '-'
        self.color = '-'
        self.barrel = '-'
        self.hopUp = '-'

    def __str__(self):
        """
        Method for splitting each attribute of Product with tabulator and adding \n at the end of each row.
        :return: Returns string containing separated attributes.
        """
        return '\t'.join((self.url, self.name, self.price, self.speed, self.mechabox, self.body, self.color, self.barrel, self.hopUp)) + '\n'

    def process_attribute(self, key, val):
        """
        Method for assigning attributes based on key value. Val is the value assigned to attribute.
        :param key: Name of attribute.
        :param val: Value of the attribute.
        """
        if key == 'Úsťová_rychlost':
            self.speed = val
        elif key == 'Mechabox':
            self.mechabox = val
        elif key == 'Materiál_těla':
            self.body = val
        elif key == 'Barva':
            self.color = val
        elif key == 'Délka_hlavně':
            self.barrel = val
        elif key == 'Hop-up_komora':
            self.hopUp = val

    def encode(self):
        """
        Method for encoding string to UTF-8 so it can be stored to STDOUT buffer.
        :return: Returns encoded string.
        """
        str = self.__str__()
        return str.encode(encoding = 'UTF-8', errors = 'strict')