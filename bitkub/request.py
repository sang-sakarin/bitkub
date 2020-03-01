import requests


def basic_request(method, url):
    return requests.request(method, url).json()
