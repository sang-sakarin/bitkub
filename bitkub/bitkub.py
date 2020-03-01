"""
A libraly that provides a python interface to Bitkub API
"""
from .constants import ENDPOINTS
from .request import basic_request


class Bitkub:
    def __init__(self, api_key=None):
        self.api_key = api_key
        self.API_ROOT = ENDPOINTS["API_ROOT"]

    def _get_path(self, path_name):
        """
        Get full endpoint for a specific path.
        """
        return self.API_ROOT + ENDPOINTS[path_name]

    def status(self):
        url = self._get_path("STATUS_PATH")

        return basic_request('GET', url)

    def servertime(self):
        url = self._get_path("SERVERTIME_PATH")

        return basic_request('GET', url)
