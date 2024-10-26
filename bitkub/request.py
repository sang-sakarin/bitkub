import requests


def basic_request(method, url, headers=None, payload=None):
    if headers is None:
        headers = {}

    if payload is None:
        payload = {}

    return requests.request(method, url, headers=headers, data=payload).json()
