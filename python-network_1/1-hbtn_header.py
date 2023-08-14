import requests
import sys

url = input("url: ")


def getheader(url):
    request = requests(url)
    return request.headers.get('X-Request-Id')
