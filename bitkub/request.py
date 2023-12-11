import requests


def basic_request(method, url, headers={}, payload={}):
    # print(url)
    resp = requests.request(method, url, headers=headers, data=payload)
    # print(resp.text)
    return resp.json()
