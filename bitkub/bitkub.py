"""
A libraly that provides a python interface to Bitkub API
"""
from .constants import ENDPOINTS
from .request import basic_request


class Bitkub:
    def __init__(self, api_key=None):
        self.api_key = api_key
        self.API_ROOT = ENDPOINTS["API_ROOT"]

    def _get_path(self, path_name, **kwargs):
        """
        Get full endpoint for a specific path.
        """
        return self.API_ROOT + ENDPOINTS[path_name].format(**kwargs)

    def status(self):
        url = self._get_path("STATUS_PATH")

        return basic_request('GET', url)

    def servertime(self):
        url = self._get_path("SERVERTIME_PATH")

        return basic_request('GET', url)

    def symbols(self):
        url = self._get_path("MARKET_SYMBOLS_PATH")

        return basic_request('GET', url)

    def ticker(self):
        url = self._get_path("MARKET_TICKER_PATH")

        return basic_request('GET', url)

    def trades(self, sym, lmt):
        url = self._get_path("MARKET_TRADES_PATH", sym=sym, lmt=lmt)

        return basic_request('GET', url)

    def bids(self, sym, lmt):
        url = self._get_path("MARKET_BIDS_PATH", sym=sym, lmt=lmt)

        return basic_request('GET', url)

    def asks(self, sym, lmt):
        url = self._get_path("MARKET_ASKS_PATH", sym=sym, lmt=lmt)

        return basic_request('GET', url)

    def books(self, sym, lmt):
        url = self._get_path("MARKET_BOOKS_PATH", sym=sym, lmt=lmt)

        return basic_request('GET', url)
