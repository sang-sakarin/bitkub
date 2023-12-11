"""
A library that provides a python interface to Bitkub API
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

    def _get_headers(self, ts='', sig=''):
        headers = {
            "ACCEPT": "application/json",
            "CONTENT-TYPE": "application/json",
            "X-BTK-TIMESTAMP": "{0}".format(ts),
            "X-BTK-APIKEY": "{0}".format(self.api_key),
            "X-BTK-SIGN": "{0}".format(sig)
        }

        return headers
    
    def _get_signature(self, method, ts, url, payload=''):
        url_path = url.replace(self.API_ROOT, '')
        message = f"{ts}{method}{url_path}" + payload
        signature = hmac.new(self._get_api_secret(), msg=message.encode(), digestmod=hashlib.sha256).hexdigest()

        return signature

    def _get_timestamp(self):
        timestamp = int(time.time())

        return timestamp

    def _get_payload(self, **kwargs):
        payload = {}
        # payload = {"ts": self._get_timestamp()}
        # payload = {"ts": self.servertime()}
        payload.update(kwargs)
        # payload["sig"] = self._get_signature(payload)
        payload = self._json_encode(payload)

        return payload
    
    def _get_swap_sym(self, sym):
        sym_swap = sym.split('_')
        sym = f'{sym_swap[1]}_{sym_swap[0]}'

        return sym

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

    def tradingview(self, sym='', resolution=1, frm='', to=''):
        frm = str(int(int(frm)/1000)) if int(frm) > 9999999999 else str(int(frm))
        to = str(int(int(to)/1000)) if int(to) > 9999999999 else str(int(to))
        url = self._get_path("MARKET_TRADING_VIEW_PATH", sym=self._get_swap_sym(sym), resolution=resolution, frm=frm, to=to)

        return basic_request('GET', url)

    def depth(self, sym='', lmt=1):
        url = self._get_path("MARKET_DEPTH_PATH", sym=sym, lmt=lmt)

        return basic_request('GET', url)

    @check_in_attributes(["api_key", "api_secret"])
    def wallet(self):
        url = self._get_path("MARKET_WALLET")
        payload = self._get_payload()
        ts = self.servertime()
        sig = self._get_signature('POST', ts, url, payload)

        return basic_request('POST', url, headers=self._get_headers(ts, sig), payload=payload)

    @check_in_attributes(["api_key", "api_secret"])
    def balances(self):
        url = self._get_path("MARKET_BALANCES")
        payload = self._get_payload()
        ts = self.servertime()
        sig = self._get_signature('POST', ts, url, payload)

        return basic_request('POST', url, headers=self._get_headers(ts, sig), payload=payload)

    @check_in_attributes(["api_key", "api_secret"])
    def place_bid(self, sym='', amt=1, rat=1, typ='limit', client_id=''):
        url = self._get_path("MARKET_PLACE_BID")
        payload = self._get_payload(sym=sym, amt=amt, rat=rat, typ=typ, client_id=client_id)
        ts = self.servertime()
        sig = self._get_signature('POST', ts, url, payload)
        
        return basic_request('POST', url, headers=self._get_headers(ts, sig), payload=payload)

    # 2023-11-29 Deprecated
    def place_bid_test(self, sym='', amt=1, rat=1, typ='limit', client_id=''):

        return None

    @check_in_attributes(["api_key", "api_secret"])
    def place_ask(self, sym='', amt=1, rat=1, typ='limit', client_id=''):
        url = self._get_path("MARKET_PLACE_ASK")
        payload = self._get_payload(sym=sym, amt=amt, rat=rat, typ=typ, client_id=client_id)
        ts = self.servertime()
        sig = self._get_signature('POST', ts, url, payload)
        
        return basic_request('POST', url, headers=self._get_headers(ts, sig), payload=payload)

    # 2023-11-29 Deprecated
    def place_ask_test(self, sym='', amt=1, rat=1, typ='limit', client_id=''):

        return None

    # 2023-03-27 Deprecated
    # mapping function form place_ask_by_fiat to place_ask
    @check_in_attributes(["api_key", "api_secret"])
    def place_ask_by_fiat(self, sym='', amt=1, rat=1, typ='limit', client_id=''):
        coin_amt = amt/rat if rat > 0 else amt
        return self.place_ask(sym=sym, amt=coin_amt, rat=rat, typ=typ, client_id=client_id)

    @check_in_attributes(["api_key", "api_secret"])
    def cancel_order(self, sym='', id='', sd='buy', hash=''):
        url = self._get_path("MARKET_CANCEL_ORDER")
        payload = self._get_payload(sym=sym, id=id, sd=sd, hash=hash)
        ts = self.servertime()
        sig = self._get_signature('POST', ts, url, payload)
        
        return basic_request('POST', url, headers=self._get_headers(ts, sig), payload=payload)

    @check_in_attributes(["api_key", "api_secret"])
    def my_open_orders(self, sym=''):
        url = self._get_path("MARKET_MY_OPEN_ORDERS", sym=self._get_swap_sym(sym))
        ts = self.servertime()
        sig = self._get_signature('GET', ts, url)
        
        return basic_request('GET', url, headers=self._get_headers(ts, sig))

    @check_in_attributes(["api_key", "api_secret"])
    def my_open_history(self, sym='', p=1, lmt=10, start=None, end=None):
        if start is None or end is None:
            url = self._get_path("MARKET_MY_ORDER_HISTORY", sym=self._get_swap_sym(sym), p=p, lmt=lmt)
        else:
            url = self._get_path("MARKET_MY_ORDER_HISTORY_STARTEND", sym=self._get_swap_sym(sym), p=p, lmt=lmt, start=start, end=end)
        ts = self.servertime()
        sig = self._get_signature('GET', ts, url)
        
        return basic_request('GET', url, headers=self._get_headers(ts, sig))

    @check_in_attributes(["api_key", "api_secret"])
    def order_info(self, sym='', id=None, sd='buy', hash=''):
        url = self._get_path("MARKET_ORDER_INFO", sym=self._get_swap_sym(sym), id=id, sd=sd, hash=hash)
        ts = self.servertime()
        sig = self._get_signature('GET', ts, url)
        
        return basic_request('GET', url, headers=self._get_headers(ts, sig))

    @check_in_attributes(["api_key", "api_secret"])
    def crypto_address(self, p=1, lmt=10):
        url = self._get_path("CRYPTO_ADDRESSES")
        payload = self._get_payload(p=p, lmt=lmt)
        ts = self.servertime()
        sig = self._get_signature('POST', ts, url, payload)
        
        return basic_request('POST', url, headers=self._get_headers(ts, sig), payload=payload)

    @check_in_attributes(["api_key", "api_secret"])
    def crypto_withdraw(self, cur='', amt=0, adr='', mem=''):
        url = self._get_path("CRYPTO_WITHDRAW")
        payload = self._get_payload(cur=cur, amt=amt, adr=adr, mem=mem)
        ts = self.servertime()
        sig = self._get_signature('POST', ts, url, payload)
        
        return basic_request('POST', url, headers=self._get_headers(ts, sig), payload=payload)

    @check_in_attributes(["api_key", "api_secret"])
    def crypto_internal_withdraw(self, cur='', amt=0, adr='', mem=''):
        url = self._get_path("CRYPTO_INTERNAL_WITHDRAW")
        payload = self._get_payload(cur=cur, amt=amt, adr=adr, mem=mem)
        ts = self.servertime()
        sig = self._get_signature('POST', ts, url, payload)
        
        return basic_request('POST', url, headers=self._get_headers(ts, sig), payload=payload)

    @check_in_attributes(["api_key", "api_secret"])
    def crypto_deposit_history(self, p=1, lmt=10):
        url = self._get_path("CRYPTO_DEPOSIT_HISTORY")
        payload = self._get_payload(p=p, lmt=lmt)
        ts = self.servertime()
        sig = self._get_signature('POST', ts, url, payload)
        
        return basic_request('POST', url, headers=self._get_headers(ts, sig), payload=payload)

    @check_in_attributes(["api_key", "api_secret"])
    def crypto_withdraw_history(self, p=1, lmt=10):
        url = self._get_path("CRYPTO_WITHDRAW_HISTORY")
        payload = self._get_payload(p=p, lmt=lmt)
        ts = self.servertime()
        sig = self._get_signature('POST', ts, url, payload)
        
        return basic_request('POST', url, headers=self._get_headers(ts, sig), payload=payload)

    @check_in_attributes(["api_key", "api_secret"])
    def crypto_generate_address(self, sym=''):
        url = self._get_path("CRYPTO_GENERATE_ADDRESS")
        payload = self._get_payload(sym=sym)
        ts = self.servertime()
        sig = self._get_signature('POST', ts, url, payload)
        
        return basic_request('POST', url, headers=self._get_headers(ts, sig), payload=payload)

    @check_in_attributes(["api_key", "api_secret"])
    def fiat_accounts(self, p=1, lmt=10):
        url = self._get_path("FIAT_ACCOUNTS")
        payload = self._get_payload(p=p, lmt=lmt)
        ts = self.servertime()
        sig = self._get_signature('POST', ts, url, payload)
        
        return basic_request('POST', url, headers=self._get_headers(ts, sig), payload=payload)

    @check_in_attributes(["api_key", "api_secret"])
    def fiat_withdraw(self, id='', amt=0):
        url = self._get_path("FIAT_WITHDRAW")
        payload = self._get_payload(id=id, amt=amt)
        ts = self.servertime()
        sig = self._get_signature('POST', ts, url, payload)
        
        return basic_request('POST', url, headers=self._get_headers(ts, sig), payload=payload)

    @check_in_attributes(["api_key", "api_secret"])
    def fiat_deposit_history(self, p=1, lmt=10):
        url = self._get_path("FIAT_DEPOSIT_HISTORY")
        payload = self._get_payload(p=p, lmt=lmt)
        ts = self.servertime()
        sig = self._get_signature('POST', ts, url, payload)
        
        return basic_request('POST', url, headers=self._get_headers(ts, sig), payload=payload)

    @check_in_attributes(["api_key", "api_secret"])
    def fiat_withdraw_history(self, p=1, lmt=10):
        url = self._get_path("FIAT_WITHDRAW_HISTORY")
        payload = self._get_payload(p=p, lmt=lmt)
        ts = self.servertime()
        sig = self._get_signature('POST', ts, url, payload)
        
        return basic_request('POST', url, headers=self._get_headers(ts, sig), payload=payload)

    @check_in_attributes(["api_key", "api_secret"])
    def market_wstoken(self):
        url = self._get_path("MARKET_WSTOKEN")
        payload = self._get_payload()
        ts = self.servertime()
        sig = self._get_signature('POST', ts, url, payload)
        
        return basic_request('POST', url, headers=self._get_headers(ts, sig), payload=payload)

    @check_in_attributes(["api_key", "api_secret"])
    def user_limits(self):
        url = self._get_path("USER_LIMITS")
        payload = self._get_payload()
        ts = self.servertime()
        sig = self._get_signature('POST', ts, url, payload)
        
        return basic_request('POST', url, headers=self._get_headers(ts, sig), payload=payload)

    @check_in_attributes(["api_key", "api_secret"])
    def user_trading_credits(self):
        url = self._get_path("USER_TRADING_CREDITS")
        payload = self._get_payload()
        ts = self.servertime()
        sig = self._get_signature('POST', ts, url, payload)
        
        return basic_request('POST', url, headers=self._get_headers(ts, sig), payload=payload)
