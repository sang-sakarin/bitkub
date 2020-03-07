"""
A libraly that provides a python interface to Bitkub API
"""
import hashlib
import hmac
import json
import time

from .constants import ENDPOINTS
from .decorators import check_in_attributes
from .request import basic_request


class Bitkub:
    def __init__(self, api_key=None, api_secret=None):
        self.api_key = api_key
        self.api_secret = api_secret
        self.API_ROOT = ENDPOINTS["API_ROOT"]

    def _get_api_secret(self):
        return self.api_secret.encode()

    def _get_path(self, path_name, **kwargs):
        """
        Get full endpoint for a specific path.
        """
        return self.API_ROOT + ENDPOINTS[path_name].format(**kwargs)

    def _json_encode(self, payload):
        return json.dumps(payload, separators=(',', ':'), sort_keys=True)

    def _get_headers(self):
        headers = {
            "ACCEPT": "application/json",
            "CONTENT-TYPE": "application/json",
            "X-BTK-APIKEY": "{0}".format(self.api_key)
        }

        return headers

    def _get_signature(self, payload):
        message = self._json_encode(payload)
        signature = hmac.new(self._get_api_secret(), msg=message.encode(), digestmod=hashlib.sha256).hexdigest()

        return signature

    def _get_timestamp(self):
        timestamp = int(time.time())

        return timestamp

    def _get_payload(self):
        payload = {}
        payload["ts"] = self._get_timestamp()

        return payload

    def set_api_key(self, api_key):
        self.api_key = api_key

    def set_api_secret(self, api_secret):
        self.api_secret = api_secret

    def status(self):
        url = self._get_path("STATUS_PATH")

        return basic_request('GET', url)

    def servertime(self):
        url = self._get_path("SERVERTIME_PATH")

        return basic_request('GET', url)

    def symbols(self):
        url = self._get_path("MARKET_SYMBOLS_PATH")

        return basic_request('GET', url)

    def ticker(self, sym=''):
        url = self._get_path("MARKET_TICKER_PATH", sym=sym)

        return basic_request('GET', url)

    def trades(self, sym='', lmt=1):
        url = self._get_path("MARKET_TRADES_PATH", sym=sym, lmt=lmt)

        return basic_request('GET', url)

    def bids(self, sym='', lmt=1):
        url = self._get_path("MARKET_BIDS_PATH", sym=sym, lmt=lmt)

        return basic_request('GET', url)

    def asks(self, sym='', lmt=1):
        url = self._get_path("MARKET_ASKS_PATH", sym=sym, lmt=lmt)

        return basic_request('GET', url)

    def books(self, sym='', lmt=1):
        url = self._get_path("MARKET_BOOKS_PATH", sym=sym, lmt=lmt)

        return basic_request('GET', url)

    def tradingview(self, sym='', int=1, frm='', to=''):
        url = self._get_path("MARKET_TRADING_VIEW_PATH", sym=sym, int=int, frm=frm, to=to)

        return basic_request('GET', url)

    def depth(self, sym='', lmt=1):
        url = self._get_path("MARKET_DEPTH_PATH", sym=sym, lmt=lmt)

        return basic_request('GET', url)

    @check_in_attributes(["api_key", "api_secret"])
    def wallet(self):
        url = self._get_path("MARKET_WALLET")
        payload = self._get_payload()
        signature = self._get_signature(payload)
        payload["sig"] = signature
        payload = self._json_encode(payload)

        return basic_request('POST', url, headers=self._get_headers(), payload=payload)
